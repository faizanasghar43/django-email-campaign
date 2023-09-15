from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from rest_framework.response import Response
import requests
import re
from bs4 import BeautifulSoup
from .models import Scrappy
from .serializers import ScrappingSerializer


class ScrappyAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        scrappies = Scrappy.objects.filter(user=request.user)
        serializer = ScrappingSerializer(scrappies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        user_id = request.user.id
        url = request.data.get('url')

        existing_entry = Scrappy.objects.filter(user=user_id, url=url).first()
        if existing_entry:
            serializer = ScrappingSerializer(existing_entry)
            return Response(serializer.data, status=status.HTTP_200_OK)

        request.data['user'] = user_id
        request.data['emails'] = scrape_emails(url)
        serializer = ScrappingSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        scrappy = Scrappy.objects.filter(user=request.user, pk=pk).first()
        if not scrappy:
            return Response({'error': 'Scrappy not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ScrappingSerializer(scrappy, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        scrappy = Scrappy.objects.filter(user=request.user, pk=pk).first()
        if not scrappy:
            return Response({'error': 'Scrappy not found.'}, status=status.HTTP_404_NOT_FOUND)

        scrappy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# def scrape_emails(url):
#     response = requests.get(url)
#     regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
#     return re.findall(regex, response.text)




def scrape_emails(url):
    response = requests.get(url)
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    urls = set()
    emails = []

    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find and extract emails from the current page
        emails += re.findall(email_regex, response.text)

        # Find all URLs on the current page
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and href.startswith('http'):  # Filter out non-http links
                urls.add(href)

    # Scrape emails from each URL found on the current page
    for url in urls:
        response = requests.get(url)
        if response.ok:
            emails += re.findall(email_regex, response.text)

    return emails
