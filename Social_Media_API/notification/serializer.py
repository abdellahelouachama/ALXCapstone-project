from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import Notification

class NotificationSerializer(ModelSerializer):
    """Serializer to handle notification data conversion."""
    # StringRelatedField is used to represent the target field as a string.
    actor = StringRelatedField(read_only=True)

    class Meta:
        model = Notification
        fields = ['actor', 'verb']