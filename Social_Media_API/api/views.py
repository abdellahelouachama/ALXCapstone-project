from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import PostSerializer
from .permissions import IsPostAuthor
from rest_framework import status
from posts.models import Post

# Post managment
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'title'
    permission_classes = [IsAuthenticated, IsPostAuthor]
     
    def list(self, request, *args, **kwargs):
        """
        http get method for list is not allowed,

        """
        return Response({'message': 'GET method for list is not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    

        