from django.urls import path
from .views import NotificationView

# url patterns for notifications
urlpatterns = [
    path('notifications/', NotificationView.as_view(), name='notifications')
]