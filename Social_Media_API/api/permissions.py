from rest_framework.permissions import BasePermission

class IsPostAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        
        """
        Check if the request.user is the author of the obj.

        Args:
            request (Request): The request object.
            view (View): The view object.
            obj (Post): The post object.

        Returns:
            bool: True if the user is the author, False otherwise.
        """
        if request.method in ['PUT', 'DELETE', 'PATCH']:
            return request.user == obj.author
        
        return True