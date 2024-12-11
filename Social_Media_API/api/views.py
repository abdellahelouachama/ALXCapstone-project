from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serailizers import UserSerializer
from .permissions import IsLoggedIn
from django.contrib.auth import get_user_model
User = get_user_model()

# User API view to retrieve, update, and delete user data, requires authentication and isLoggedIn permission
# note: the user creation is handled in the Register view in the user app
class UserAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsLoggedIn]
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
        
        
