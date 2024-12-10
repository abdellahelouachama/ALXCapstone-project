from rest_framework.generics import UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .serializer import UserSerilizer
from django.contrib.auth import get_user_model
User = get_user_model()

class UserApiView(UpdateAPIView, DestroyAPIView, RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerilizer
    lookup_field = 'username'
    # permission_classes = [IsAuthenticated]