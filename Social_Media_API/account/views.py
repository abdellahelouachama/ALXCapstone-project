from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .serializers import UserSerializer, UserFollowSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from account.models import Followers
from .permissions import IsAccountOwner
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.decorators import action
from django.contrib.auth import get_user_model
User = get_user_model()



# Register view to handle the creation of a new user
class RegisterView(APIView):
    def post(self, request):
        """
        Handle the creation of a new user.

        Args:
            request (Request): The request body with the user details.

        Returns:
            Response: A response with the result of the registration.

        Raises:
            Exception: If the registration of the user failed.
        """
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        first_name = request.data.get("first_name", "")
        last_name = request.data.get("last_name", "")
        profile_picture = request.data.get("profile_picture", None)
        bio = request.data.get("bio", "")

        if not username or not email or not password:
            return Response({'error':'Username, email, and password are required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                bio=bio,
                profile_picture=profile_picture,
            )
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# Login view to handle user login and token generation
class LoginView(APIView):
    def post(self, request):
        """
        Handle the login of a user.

        Args:
            request (Request): The request body with the user credentials.

        Returns:
            Response: A response with the result of the login and token.

        Raises:
            Exception: If the login of the user failed.
        """
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error':'Username and Password are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(request=request, username=username, password=password)

        if user is not None:

            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {
                    'message':'Login successful',
                    'token': token.key
                },
                status=status.HTTP_200_OK
            )
        
        else:
            return Response({'error':'Invalid credentials.'}, status=status.HTTP_400_BAD_REQUEST)

# Logout view to handle user logout and token deletion
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        
        """
        Handle the logout of a user by deleting the authentication token.

        Args:
            request (Request): The request object containing the user information.

        Returns:
            Response: A response indicating the success or failure of the logout operation.
        """
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response({'message': 'Logout successful.'}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({'error': 'Token does not exist.'}, status=status.HTTP_400_BAD_REQUEST)



# User Profile managment 
# User API view to retrieve, update, and delete user data, requires authentication and isLoggedIn permission
# Note: the user creation is handled in the Register view as a part of authentication system
class UserAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAccountOwner]
    lookup_field = 'username'

    def get_object(self):
        """
    Retrieve and return the user object based on the username lookup field.

    Checks the permissions for the retrieved object before returning it.

    Returns:
        User: The user object if permissions are granted and the object is found.
        """
        obj =  super().get_object()
        self.check_object_permissions(self.request, obj)
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
        user = self.queryset.get(username=username)
        
        # check if the user is trying to follow themselves
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
        followed_user = self.queryset.get(username=username)
        
        try:
            # check if the user is following the followed user
            instance = Followers.objects.get(follower=request.user, followed=followed_user)

        except Followers.DoesNotExist:
            return Response({'error': 'You are not following this user'}, status=status.HTTP_404_NOT_FOUND) 
        
        # delete the follow
        instance.delete()
        return Response({'message': 'Unfollowed successfully'}, status=status.HTTP_200_OK)
