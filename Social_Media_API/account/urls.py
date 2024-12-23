from django.urls import path
from . import views


# url patterns for the user authentication
urlpatterns = [
    # url for registering a new user
    path('register/', views.RegisterView.as_view(), name='register'),
    # url for logging in a user
    path('login/', views.LoginView.as_view(), name='login'),
    # url for logging out a user
    path('logout/', views.LogoutView.as_view(), name='logout'),

]

# url patterns for the user profile
urlpatterns += [
    # these url patterns handle all the user operations(retrieve, partial update, update, delete)
    # and based on the request method the appropriate view will be called (GET, PUT, PATCH, DELETE)
    # we used the same url pattern for all user actions, but we diffentiate them based on the request method 
    path('profile/<username>/', views.UserAPIView.as_view(), name='user'),
    
    # Url for following and unfollowing a user
    path('follow/<username>/', views.FollowAPIView.as_view({'post':'follow'}), name='follow'),
    path('unfollow/<username>/', views.FollowAPIView.as_view({'delete':'unfollow'}), name='unfollow'),
]
