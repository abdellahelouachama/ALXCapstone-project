from django.urls import path
from .views import UserAPIView


# url patterns for the user views
urlpatterns = [
    # this url pattern handle all the user operation(retrieve, update, delete)
    # and based on the request method the appropriate view will be called (GET, PUT, PATCH, DELETE)
    path('users/<username>', UserAPIView.as_view(), name='user')
]