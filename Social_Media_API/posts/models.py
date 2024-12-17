from django.db import models
from django.contrib.auth import get_user_model
User =get_user_model()

# Post model 
class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, unique=True)
    content = models. TextField(max_length=1000, null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    