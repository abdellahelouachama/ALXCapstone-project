from django.contrib.auth import get_user_model
from django.db import models
User =get_user_model()

# # Post model with title, content, author, created_at, updated_at fields
class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, unique=True)
    content = models. TextField(max_length=1000, null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """
        Returns the title of the post as a string.

        Returns:
            str: The title of the post.
        """
        return self.title

# like model with user, post, created_at fields
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

# comment model with author, post, content, created_at fields
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=1000, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content