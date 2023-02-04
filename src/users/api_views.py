from django.contrib.auth import authenticate, login, logout, get_user_model
from django.core.validators import validate_email
from django.contrib.auth import authenticate

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.request import Request

from drf_yasg.utils import swagger_auto_schema

from .serializer import UserSerializer


User = get_user_model()

class SignUpView(generics.GenericAPIView):
    serializer_class = UserSerializer
    
    @swagger_auto_schema(
        operation_summary="L'api pour l'enregistrement d'un utilisateur ",
        operation_description=" Cette Api crée un user avec differents champs"
    )
    def post(self, request:Request):
        data = request.data
        
        serializer = self.serializer_class(data=data)
        
        if serializer.is_valid():
            serializer.save()
            
            response = {
                "message": "L'utlisateur est bel et bien enregistré",
                "data": serializer.data
            }
            
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    @swagger_auto_schema(
        operation_summary="L'api de connexion",
        operation_description=" Cette Api permet au user de s'authentifier avec le username et le mot de passe"
    )
    def post(self, request:Request):
        username = request.data.get('username')
        password = request.data.get('password')
        my_user = User.objects.get(username=username)
        
        if my_user.is_active:
            user = authenticate(username=username, password=password)
            print(user)
            
            if user is not None:
                response = {
                    "message": "vous etes connecté",
                    "token":  user.auth_token.key,
                    "username": user.username,
                }
                return Response(data=response, status=status.HTTP_200_OK)
            else:
                return Response(data={"message":"username ou mot de passe incorrect",})

        return Response(data={"message": "votre compte n'est pas actif, veuillez contacter l'admin"})
        
    
    @swagger_auto_schema(
        operation_summary="L'api de connexion(verification)",
        operation_description=" Cette Api permet de verifier si le user est autifier \ndans le cas contraire il renvoie Anonymos\n{\n \t \"user\": \"Anonymos,\"\n \t\"auth\":None\n}"
    )
    def get(self, request:Request):
        content = {
            "user": str(request.user),
            "auth": str(request.auth)
        }
        
        return Response(data=content, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def sign_out(request):
    message = ''

    request.user.auth_token.delete()
    logout(request)
    message = 'utilisateur déconnecté'

    return Response({'mesdage':message})