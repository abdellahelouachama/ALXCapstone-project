from django.urls import path
from . import views

# url patterns for the authentication views
urlpatterns = [
    # url for registering a new user
    path('register/', views.RegisterView.as_view(), name='register'),
    # url for logging in a user
    path('login/', views.LoginView.as_view(), name='login'),
    # url for logging out a user
    path('logout/', views.LogoutView.as_view(), name='logout')
]
