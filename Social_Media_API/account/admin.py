from django.contrib import admin
from .models import CustomUser, Followers

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name']

@admin.register(Followers)
class UserFollowAdmin(admin.ModelAdmin):
    list_display = ['follower', 'followed', 'created_at']
