from django.urls import path
from .views import UserAPIView


urlpatterns = [
    path('users/<username>', UserAPIView.as_view(), name='user')
]