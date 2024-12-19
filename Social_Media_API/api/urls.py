from rest_framework.routers import DefaultRouter
from .views import PostViewSet, FeedAPIView, CommentViewSet
from django.urls import path

# Register the PostViewSetn, CommentViewSet with router
router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

# url patterns
urlpatterns = [
    # url for the feed
    path('feed/', FeedAPIView.as_view({'get':'feed'}), name='feed')
]

urlpatterns += router.urls
