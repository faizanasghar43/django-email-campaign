import re
from django.utils import timezone
from django_q.models import Schedule
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import CampaignSerializer
from .models import Campaign
from email_scrapping.models import Scrappy


class CampaignView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.data['user'] = request.user.id
        serializer = CampaignSerializer(data=request.data)

        if not serializer.is_valid(raise_exception=True):
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data)

    def get(self, request):
        user_id = request.user.id

        if request.query_params:
            campaigns = Campaign.objects.filter(user=user_id, **request.query_params.dict())
        else:
            campaigns = Campaign.objects.filter(user=user_id)

        if campaigns:
            serializer = CampaignSerializer(campaigns, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CampaignDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            campaign = Campaign.objects.get(id=pk)
            serializer = CampaignSerializer(instance=campaign)
            return Response(serializer.data)
        except Campaign.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        campaign = Campaign.objects.get(id=pk)
        data = CampaignSerializer(instance=campaign, data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        campaign = get_object_or_404(Campaign, id=pk)
        campaign.delete()
        return Response("Successfully deleted", status=status.HTTP_202_ACCEPTED)


class CampaignSchedulerView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, campaign_id):
        scrapped_emails = Scrappy.objects.filter(user=request.user)
        email_list = []
        for scrapped_email in scrapped_emails:
            email_list.extend(scrapped_email.emails.split(','))

        email_pattern = r'\'?([\w\.-]+@[\w\.-]+)\'?'
        email_list = re.findall(email_pattern, ' '.join(email_list))

        Schedule.objects.create(
            name="Test scheduling new 1",
            func="campaigns.task.send_campaign_email",
            args=f'{campaign_id},{email_list}',
            next_run=timezone.now(),
        )

        return Response({'Campaign scheduled successfully, Emails are being sent on ': email_list})
