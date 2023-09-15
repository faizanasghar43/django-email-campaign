from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from users.serializers import UserSeraializer
from rest_framework.response import Response


class RegisterUser(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = UserSeraializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status': 403, 'errors': serializer.errors, 'message': 'Something went wrong'})
        serializer.save()
        user = User.objects.get(username=serializer.data['username'])
        print(user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({
           'status': 200, 'payload': serializer.data, 'token': str(token), 'message': 'your data has been saved'
        })
