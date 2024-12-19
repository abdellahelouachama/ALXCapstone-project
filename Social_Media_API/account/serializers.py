from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from account.models import Followers
User = get_user_model()

# User Serializer to handle user data conversion (serialization, deserialization)
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

# User follow Serializer to handle UserFollow model data conversion (serialization, deserialization)
class UserFollowSerializer(ModelSerializer):
    class Meta:
        model = Followers
        fields = '__all__'