from django.urls import path
from .views import UserAPIView


# url patterns for the user viewset
urlpatterns = [
    # this url pattern handle all the user operations(retrieve, partial update, update, delete)
    # and based on the request method the appropriate view will be called (GET, PUT, PATCH, DELETE)
    path('users/<username>', UserAPIView.as_view({'get': 'retrieve'}), name='user'),
    path('users/<username>', UserAPIView.as_view({'put': 'update'}), name='user'),
    path('users/<username>', UserAPIView.as_view({'patch': 'partial_update'}), name='user'),
    path('users/<username>', UserAPIView.as_view({'delete': 'destroy'}), name='user'),
    # custom actions follow and unfollow
    path('users/<username>/follow', UserAPIView.as_view({'post': 'follow'}), name='follow'),
    path('users/<username>/unfollow', UserAPIView.as_view({'delete':'unfollow'}), name='unfollow'),
]