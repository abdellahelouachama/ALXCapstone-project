from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import status
from django.contrib.auth import get_user_model
User = get_user_model()

# Register view to handle the creation of a new user
class RegisterView(APIView):
    def post(self, request):
        """
        Handle the creation of a new user.

        Args:
            request (Request): The request body with the user details.

        Returns:
            Response: A response with the result of the registration.

        Raises:
            Exception: If the registration of the user failed.
        """
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        first_name = request.data.get("first_name", "")
        last_name = request.data.get("last_name", "")
        profile_picture = request.data.get("profile_picture", None)
        bio = request.data.get("bio", "")

        if not username or not email or not password:
            return Response({'error':'Username, email, and password are required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                bio=bio,
                profile_picture=profile_picture,
            )
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# Login view to handle user login and token generation
class LoginView(APIView):
    def post(self, request):
        """
        Handle the login of a user.

        Args:
            request (Request): The request body with the user credentials.

        Returns:
            Response: A response with the result of the login and token.

        Raises:
            Exception: If the login of the user failed.
        """
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error':'Username and Password are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(request=request, username=username, password=password)

        if user is not None:

            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {
                    'message':'Login successful',
                    'token': token.key
                },
                status=status.HTTP_200_OK
            )
        
        else:
            return Response({'error':'Invalid credentials.'}, status=status.HTTP_400_BAD_REQUEST)

# Logout view to handle user logout and token deletion
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        
        """
        Handle the logout of a user by deleting the authentication token.

        Args:
            request (Request): The request object containing the user information.

        Returns:
            Response: A response indicating the success or failure of the logout operation.
        """
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response({'message': 'Logout successful.'}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({'error': 'Token does not exist.'}, status=status.HTTP_400_BAD_REQUEST)