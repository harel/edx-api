from django.urls import path
from django.conf import settings
from .api import UsersAPIView, RefreshToken


urlpatterns = [
    path('/api-edx/users/', UsersAPIView.as_view()),
    path('/api-edx/token/', RefreshToken.as_view()),
]
