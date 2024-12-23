from rest_framework.permissions import BasePermission

class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        Check if the user is the author of the post or comment.

        Args:
            request (Request): The request object.
            view (View): The view object.
            obj (Post): The post, or comment object, .

        Returns:
            bool: True if the user is the author of the post or comment, False otherwise.
        """
        if request.method in ['PUT', 'DELETE', 'PATCH'] and view.action in ['update', 'destroy']:
            return request.user == obj.author
        
        return True