from django.shortcuts import render

# Create your views here.
from .models import Usuario
from rest_framework.response import Response
from .serializers import UsuarioSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import AuthenticationFailed
from passlib.hash import pbkdf2_sha256
import jwt, datetime
# Create your views here.

class UsuarioApiView(APIView):
  
  def post(self, request):
      #if request.method == 'POST':
        usuario_serializer = UsuarioSerializer(data=request.data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return Response(usuario_serializer.data, status=status.HTTP_201_CREATED)
        return Response(usuario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


  def get(self,request, pk=None, format=None):
        if pk:
            usuario= get_object_or_404(Usuario.objects.all(),pk=pk)
            usuario_serializer = UsuarioSerializer(usuario, many=False)
            return Response(usuario_serializer.data)
        usuarios= Usuario.objects.all()
        usuarios_serializer=UsuarioSerializer(usuarios,many=True)
        return Response(usuarios_serializer.data)

  def put(self, request, pk):
        usuario = get_object_or_404(Usuario.objects.all(),pk=pk)
        usuario_serializer = UsuarioSerializer(usuario, data=request.data, many=False)
        if usuario_serializer.is_valid(raise_exception=True):
            usuario_serializer.save()
            return Response(usuario_serializer.data)
        return Response(usuario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  def patch(self, request, pk):
        usuario = get_object_or_404(Usuario.objects.all(),pk=pk)
        usuario_serializer = UsuarioSerializer(usuario, data=request.data, partial=True) # set partial=True to update a data partially
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return Response(usuario_serializer.data)
        return Response(usuario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

       
class LoginView(APIView):

    def post(self,request):
        correo= request.data['correo']
        contrasenia = request.data['contrasenia']

        user= Usuario.objects.filter(correo=correo).first()
        contra= Usuario.objects.filter(contrasenia=contrasenia).first()
        #contra=pbkdf2_sha256.hash(Usuario.objects.filter(contrasenia=contrasenia).first())
        if user is None:
            raise AuthenticationFailed('User not found!')
            #pa verificar desde el hash
        if contra is None:
            raise AuthenticationFailed('incorrect password')
        



        #create a jwt
    
        payload={
            'id':user.idusuario,
            'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=60),
            'iat':datetime.datetime.utcnow()
        }


        token= jwt.encode(payload,'secret',algorithm='HS256')
    
         #return jwt via cookies
        response=  Response()

        response.set_cookie(key='jwt', value=token,httponly= True,)

        response.data={
            'jwt': token
        }
        return response


class UsuarioView(APIView):
    
    def get (self,request):

        token= request.COOKIES.get('jwt')

        #decoded to get te user
        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload= jwt.decode(token,'secret',algorithms=['HS256'])
            

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')

        user = Usuario.objects.filter(idusuario=payload['id']).first()

        serializer=UsuarioSerializer(user)

        return Response(serializer.data)

class LogoutView(APIView):

    def post(self,request):
        response= Response()
        response.delete_cookie('jwt')
        response.data={
            'message':'success logout'
        }
        return response