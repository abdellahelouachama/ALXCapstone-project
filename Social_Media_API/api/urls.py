from django.urls import path
from .views import UserAPIView


# url patterns for the user viewset
urlpatterns = [
    # this url pattern handle all the user operations(retrieve, partial update, update, delete)
    # and based on the request method the appropriate view will be called (GET, PUT, PATCH, DELETE)
    path('users/<username>', UserAPIView.as_view(), name='user')
]