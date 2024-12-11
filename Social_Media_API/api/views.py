from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serailizers import UserSerializer
from .permissions import IsLoggedIn
from django.contrib.auth import get_user_model
User = get_user_model()

class UserAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsLoggedIn]
    lookup_field = 'username'

    def get_object(self):
        obj =  super().get_object()
        self.check_object_permissions(self.request, obj)
        return obj
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "Deleted successfully."}, 
            status=status.HTTP_200_OK
        )

    def perform_destroy(self, instance):
        instance.delete()
        
        
