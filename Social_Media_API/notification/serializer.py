from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import Notification

# Notification serializer
class NotificationSerializer(ModelSerializer):
    actor = StringRelatedField(read_only=True)
    class Meta:
        model = Notification
        fields = ['actor', 'verb']