"""
pagination.py

This module defines a custom pagination class for the Social Media API.

Classes:
    CustomPagination(PageNumberPagination): A custom pagination class that sets the default page size.

Usage:
    This class can be used to paginate querysets in Django REST Framework views by setting it as the pagination class.

Example:
    from .pagination import CustomPagination
    from rest_framework.generics import ListAPIView

    class MyListView(ListAPIView):
        queryset = MyModel.objects.all()
        serializer_class = MyModelSerializer
        pagination_class = CustomPagination
"""

from rest_framework.pagination import PageNumberPagination

# Custom pagination
class CustomPagination(PageNumberPagination):
    page_size = 10
