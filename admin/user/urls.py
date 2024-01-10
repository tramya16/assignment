# urls.py

from django.urls import path
from .views import UserRegisterView, UserLoginView

urlpatterns = [
    path('register', UserRegisterView.as_view(), name='user-register'),
    path('login', UserLoginView.as_view(), name='user-login'),
]
