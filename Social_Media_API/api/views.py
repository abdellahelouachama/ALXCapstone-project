from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsAuthor
from account.models import Followers
from rest_framework import status
from .pagination import CustomPagination
from posts.models import Post, Like, Comment
from django.contrib.auth import get_user_model
User = get_user_model()

# Post managment
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'title'
    permission_classes = [IsAuthenticated, IsAuthor]
     
    def list(self, request, *args, **kwargs):
        """
        http get method for list is not allowed,

        """
        return Response({'message': 'GET method for list is not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    @action(methods=['POST'], detail=True, url_path='like')
    def like(self, request, title=None):
        """
    Like a post.

    This action allows the authenticated user to like a specific post identified by the URL parameter.
    A Like object is created associating the user with the post.

    Args:
        request: The HTTP request object containing user and post information.

    Returns:
        Response: A JSON response with a success message and a 201 status code if the like is successful,
        otherwise a response with an error message and a 400 status code if the post is not found.
        """

        post = self.get_object()
        user = request.user

        if post:

            if not Like.objects.filter(user=user, post=post).exists():

                Like.objects.create(user=user, post=post)
                # Note: when a user like a post successfuly, we have to generate notification (developed later)
                return Response({"message":"Successful liking"}, status=status.HTTP_201_CREATED)
            
            else:
                return Response({"error":"You can't like this post tiwce"}, status=status.HTTP_400_BAD_REQUEST)
  
        return Response({'error':'No Post Found Matching This Title'}, status=status.HTTP_404_NOT_FOUND)
    
    @action(methods=['DELETE'], detail=True, url_path='unlike')
    def unlike(self, request, title=None):    
        """
    Unlike a post.

    This action allows the authenticated user to unlike a specific post identified by the URL parameter.
    If the like exists, it is deleted, otherwise an error message is returned.

    Args:
        request: The HTTP request object containing user and post information.

    Returns:
        Response: A JSON response with a success message and a 200 status code if the unlike is successful,
        otherwise a response with an error message and a 404 status code if the post is not found or not liked.
        """
        post = self.get_object()
        user = request.user
        if not post:
            return Response({"error":"No Post Found Matching This Title"}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            like = Like.objects.get(user=user, post=post)

        except Like.DoesNotExist:
            return Response({"error":"You have not liked this post"}, status=status.HTTP_404_NOT_FOUND)
        
        else:
            like.delete()
            return Response({"message":"Successful unliking"}, status=status.HTTP_200_OK)

    
# Feed of Posts 
class FeedAPIView(GenericViewSet):
    queryset = Post.objects.all().order_by('-created_at') 
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def get_queryset(self):
    
        """
        Get the queryset of posts for the current user. The queryset is a collection of posts
        created by users that the current user follows. The posts are ordered by the most
        recent ones first. If the 'title' parameter is provided, the queryset is filtered to
        only include posts with that title, if title is not provided, all posts are returned.

        Returns:
            Queryset: A queryset of posts ordered by the most recent ones first.
        """
        user = self.request.user
        followed_users = Followers.objects.filter(follower=user.id).values('followed')

        title = self.request.query_params.get('title')
        filterd_posts = self.queryset.filter(author__in=followed_users)

        if title is not None:
            filterd_posts = filterd_posts.filter(title=title)
        
        return filterd_posts

    @action(detail=False, methods=['GET'], url_path='feed')
    def feed(self, request):       
        """
        Get the feed of posts for the current user. The feed is a collection of posts
        created by users that the current user follows. The posts are ordered by the most
        recent ones first. If the 'title' parameter is provided, the feed is filtered to
        only include posts with that title, if title is not provided, all posts are returned.

        Returns:
            Response: A response with the feed of posts ordered by the most recent ones first.
        """
        posts_feed = self.get_queryset()
        page = self.paginate_queryset(posts_feed)
        
        
        if page is not None:
            serializer = self.get_serializer(posts_feed, many=True)
            return self.get_paginated_response(serializer.data)
        
        return Response({"message": "No posts found."}, status=status.HTTP_204_NO_CONTENT)


# Comment viewset to handle comment operations
class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthor]
    
    def get_queryset(self):      
        """
    Retrieve a queryset of comments filtered by author or post.

    This method retrieves comments based on the optional query parameters 'author' or 'post'.
    If the 'author' parameter is provided, it filters comments by the specified author's username.
    If the 'post' parameter is provided, it filters comments by the specified post's title.
    If neither parameter is provided, it returns all comments.

    Returns:
        QuerySet: A queryset of filtered comments if the author or post is found,
                  otherwise None if the specified author or post does not exist,
                  or all comments if no parameters are provided.
        """

        author = self.request.query_params.get('author')
        post = self.request.query_params.get('post')   
            
        if author is not None:
            try:  

                author = User.objects.get(username=author)
                comments_by_author = self.queryset.filter(author=author.id)
                return comments_by_author
            
            except User.DoesNotExist:
                return None
          
        elif post is not None:
            try:

                post = Post.objects.get(title=post)
                comments_for_post = self.queryset.filter(post=post.id)
                return comments_for_post
            
            except Post.DoesNotExist:
                return None
        
        return self.queryset

    def create(self, request, *args, **kwargs):
        
        """
        Create a new Comment object with the given validated data and associate it
        with the user making the request.

        Args:
            request (Request): The request body with the comment details.

        Returns:
            Response: A response with the result of the comment creation and a 201 status code if the comment is successful,
            otherwise a response with an error message and a 400 status code if the comment is not created.
        """

        post = request.data.get('post')
        content = request.data.get('content')
        author = request.user
        
        comment_data = {'author':author.id ,'post':post, 'content':content}
        serializer =self.get_serializer(data=comment_data)

        if serializer.is_valid():
            self.perform_create(serializer)

            # Note: when a user comment on a post successfuly, we have to generate notification (developed later)
            return Response({"message":"Commented successfully"}, status=status.HTTP_201_CREATED)
        
        return Response({"error":"Comment Failed"}, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, *args, **kwargs):     
        """
        Update an existing Comment object with the given validated data and associate it
        with the user making the request.

        Args:
            request (Request): The request body with the comment details.
            *args: Additional positional arguments
            **kwargs: Additional keyword arguments

        Returns:
            Response: A response with the result of the comment update and a 200 status code if the update is successful,
            otherwise a response with an error message and a 400 status code if the update is not successful.
        """
        # Get the partial update flag (to handle PATCH and PUT properly)
        partial = kwargs.pop('partial', False)

        # Get the instance to be updated
        instance = self.get_object()

        # Modify the request data to include the logged-in user as the author if not provided
        data = request.data.copy()  # Copy the data to make it mutable
        if 'author' not in data or not data['author']:
            data['author'] = request.user.id  # Use the logged-in user's ID

        # Deserialize and validate the data
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data, status=status.HTTP_200_OK) 
    