from rest_framework.permissions import BasePermission

# Custom permission to ensure the logged-in user is the owner of the account.
class IsAccountOwner(BasePermission):
    def has_object_permission(self, request, view, obj):  
        
        """
        Custom permission to ensure the logged-in user is the owner of the account.
        """
        return request.user == obj

    