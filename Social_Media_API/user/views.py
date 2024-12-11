from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterView(APIView):
    def post(self, request):
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

class LoginView(APIView):
    def post(self, request):
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


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response({'message': 'Logout successful.'}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({'error': 'Token does not exist.'}, status=status.HTTP_400_BAD_REQUEST)