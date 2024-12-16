from django.urls import path
from . import views


# url patterns for the authentication system views
urlpatterns = [
    # url for registering a new user
    path('register/', views.RegisterView.as_view(), name='register'),
    # url for logging in a user
    path('login/', views.LoginView.as_view(), name='login'),
    # url for logging out a user
    path('logout/', views.LogoutView.as_view(), name='logout'),

]

# url patterns for the user viewset
urlpatterns += [
    # this url pattern handle all the user operations(retrieve, partial update, update, delete)
    # and based on the request method the appropriate view will be called (GET, PUT, PATCH, DELETE)
    path('profile/<username>', views.UserAPIView.as_view(), name='user'),
    
    # custom actions follow and unfollow
    path('profile/<username>/follow', views.UserAPIView.as_view(), name='follow'),
    path('profile/<username>/unfollow', views.UserAPIView.as_view(), name='unfollow'),
]
