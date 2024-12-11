from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, UserFollowSerializer
# from .permissions import IsLoggedIn
from user.models import UserFollow
from django.contrib.auth import get_user_model
User = get_user_model()

# User API view to retrieve, update, and delete user data, requires authentication and isLoggedIn permission
# note: the user creation is handled in the Register view in the user app
class UserAPIView(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'username'

    def get_object(self):
        """
    Retrieve and return the user object based on the username lookup field.

    Checks the permissions for the retrieved object before returning it.

    Returns:
        User: The user object if permissions are granted and the object is found.
        """
        obj =  super().get_object()
        # self.check_object_permissions(self.request, obj)
        return obj
    
    def destroy(self, request, *args, **kwargs):
        """
    Custom destroy method to return a 200 status code with a success message
    instead of the default 204 status code with an empty response.

    Args:
        request: The request object
        *args: Additional positional arguments
        **kwargs: Additional keyword arguments

    Returns:
        Response: A response with a success message and a 200 status code
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "Deleted successfully."}, 
            status=status.HTTP_200_OK
        )

    def perform_destroy(self, instance):
        """
        Destroy the given user object.

        Args:
            instance: The user object to be deleted
        """
        instance.delete()
    # custom action to follow a user    
    @action(detail=True, methods=['POST'], url_path='follow')
    def follow(self, request, username=None):
        """
        Follow a user.

        Args:
            request: The request object containing the user information.

        Returns:
            Response: A response with a success message and a 201 status code if the follow is successful, otherwise a response with an error message and a 400 status code.
        """
        # get the followed user
        user = self.get_object()
        
        # check if the user is following themselves
        if user == request.user:
            return Response({'error': 'You cannot follow yourself.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # create the follow
        follow_data = {'follower': request.user.id, 'followed': user.id}
        serializer = UserFollowSerializer(data=follow_data)
        
        # check if the data is valid
        if serializer.is_valid():
            serializer.save()
            return Response ({'message':'followed successfully'}, status=status.HTTP_201_CREATED)
        
        return Response ({'error':'follow failed'}, status=status.HTTP_400_BAD_REQUEST)        

     
     # custom action to unfollow a user
    @action(detail=True, methods=['DELETE'], url_path='unfollow')
    def unfollow(self, request, username=None):        
        """
    Unfollow a user

    Deletes the UserFollow object that links the request.user to the followed user.

    Args:
        request: The request object

    Returns:
        Response: A response with a success message and a 200 status code
        """
        # get the followed user
        followed_user = self.get_object()
        
        try:
            # check if the user is following the followed user
            instance = UserFollow.objects.get(follower=request.user, followed=followed_user)

        except UserFollow.DoesNotExist:
            return Response({'error': 'You are not following this user'}, status=status.HTTP_404_NOT_FOUND) 
        # delete the follow
        instance.delete()
        return Response({'message': 'Unfollowed successfully'}, status=status.HTTP_200_OK)




