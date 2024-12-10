from django.urls import path
from .views import UserApiView



urlpatterns = [
   path('users/<username>',UserApiView.as_view(), name="user-detail")
]