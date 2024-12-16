from rest_framework.permissions import BasePermission

# Custom permission 
class IsLoggedIn(BasePermission):
    def has_object_permission(self, request, view, obj):
      
        """
    Returns True if the request.user is the same as the obj user, 
    only allowing the user to perform certain actions on their own data.

    Args:
        request (Request): The request object containing the user information.
        view (View): The view object.
        obj (User): The user object.

    Returns:
        bool: True if the request.user is the same as the obj user, otherwise False.
        """
        return request.user == obj

    