from rest_framework.pagination import PageNumberPagination

# Custom pagination class to set the page size to 10
class CustomPagination(PageNumberPagination):
    page_size = 10
