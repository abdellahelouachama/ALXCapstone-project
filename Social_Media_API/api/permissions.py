from rest_framework.permissions import BasePermission

# Custom permission 
class IsLoggedIn(BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        Check if the authenticated user is the same as the object being accessed.

        Args:
            request (Request): The request object containing the user information.
            view (View): The view being accessed.
            obj (Any): The object being accessed.

        Returns:
            bool: True if the authenticated user is the same as the object being accessed, False otherwise.
        """

        return request.user == obj
    