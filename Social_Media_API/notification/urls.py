from django.urls import path
from .views import NotificationView

# url patterns
urlpatterns = [
    path('notifications/', NotificationView.as_view(), name='notifications')
]