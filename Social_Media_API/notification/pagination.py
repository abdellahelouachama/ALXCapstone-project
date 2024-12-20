from rest_framework.pagination import PageNumberPagination

# Custom pagination
class CustomPagination(PageNumberPagination):
    page_size = 10
