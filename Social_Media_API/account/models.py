from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractUser
from Social_Media_API import settings
from django.db import models

# Custom user manager to handle user creation and superuser creation
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        """
    Creates and saves a User with the given username, email, and password.

    Args:
        username (str): The username for the user.
        email (str): The email address for the user.
        password (str, optional): The password for the user. Defaults to None.
        **extra_fields: Additional fields to include in the user creation.

    Raises:
        ValueError: If the username or email is not provided.

    Returns:
        CustomUser: The created user instance.
        """
        if not username:
            raise ValueError("The username field must be set")
        if not email:
            raise ValueError("The email field must be set")
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        """
    Creates and saves a superuser with the given username and password.

    Args:
        username (str): The username for the superuser.
        password (str): The password for the superuser.
        **extra_fields: Additional fields to include in the superuser creation.

    Returns:
        CustomUser: The created superuser instance.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(username, password, **extra_fields)

# Follower model to track followers and following
class Followers(models.Model):
    follower = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='following', on_delete=models.CASCADE
    )
    followed = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='followers', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """
        Returns the follower and followed user as a string.
        """
        return f"{self.follower} follows {self.followed}"

# Custom user model to extend the AbstractUser model
class CustomUser(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    profile_picture = models.ImageField(upload_to='uploads/', null=True, blank=True)
    bio = models.TextField(max_length=1000, null=True, blank=True)
    

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()
    
    def __str__(self):
        """
        Returns the username of the user as a string.

        Returns:
            str: The username of the user.
        """
        return self.username  