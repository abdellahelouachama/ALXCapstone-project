from rest_framework.serializers import ModelSerializer,  StringRelatedField
from posts.models import Post, Comment

# Post serializer to handle data conversion (serialization, diserialization)
class PostSerializer(ModelSerializer):
    author_name = StringRelatedField(source='author', read_only=True)
    class Meta:
        model = Post
        fields = ['title', 'content', 'author_name', 'created_at']
    
    def create(self, validated_data):
        """
        Create a new Post object with the given validated data and associate it
        with the user making the request.
        """
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)
    
    def update(self, instance, validated_data):

        """
    Update an existing Post object with the given validated data and 
    associate it with the user making the request.

    Args:
        instance (Post): The Post instance to be updated.
        validated_data (dict): The validated data to update the Post instance with.

    Returns:
        Post: The updated Post instance.
        """

        validated_data['author'] = self.context['request'].user
        return super().update(instance, validated_data)
    
# Comment serializer for data conversion
class CommentSerializer(ModelSerializer):
    post_title = StringRelatedField(source='post', read_only=True)
    author_name = StringRelatedField(source='author', read_only=True)

    class Meta:
        model = Comment
        fields = ['post_title', 'post', 'author', 'author_name', 'content']
        extra_kwargs = {
            'post': {'write_only': True},  # Hide 'post' in the response
            'author': {'write_only': True}, # Hide 'author' in the response
        }
