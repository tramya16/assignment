# views.py
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password, check_password
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer,UserLoginSerializer

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        # Hash the password before saving the user
        serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
        serializer.save()


class UserLoginView(APIView):
    @swagger_auto_schema(request_body=UserLoginSerializer)
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = User.objects.get(email=email)
        if check_password(password, user.password):
            return Response({'success': 'User logged in successfully'})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)


