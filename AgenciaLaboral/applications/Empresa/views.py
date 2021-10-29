from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from .models import Empresa
from .serializers import EmpresaSerializer

from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status

import jwt, datetime
class EmpresaApiView(APIView):
   
  def get(self, request, pk=None): 
        if pk:
            empresa = get_object_or_404(Empresa.objects.all(), pk=pk)
            serializer = EmpresaSerializer(empresa)
            return Response( serializer.data)
        empresas = Empresa.objects.all()
        serializer = EmpresaSerializer(empresas, many=True)
        return Response(serializer.data)

  def post(self, request):
        empresa = request.data
        serializer = EmpresaSerializer(data=empresa)
        if serializer.is_valid(raise_exception=True):
            empresa_saved = serializer.save()
        return Response({"success": "Empresa '{}' created successfully".format(empresa_saved.nombrecomercial)})
  
  def put(self, request, pk):
        saved_empresa = get_object_or_404(Empresa.objects.all(), pk=pk)
        data = request.data
        serializer = EmpresaSerializer(instance=saved_empresa, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            empresa_saved = serializer.save()
        return Response({"success": "Empresa '{}' updated successfully".format(empresa_saved.nombrecomercial)})
  
  def delete(self, request, pk):
        empresa = get_object_or_404(Empresa.objects.all(), pk=pk)
        empresa.delete()
        return Response({"message": "Empresa with id `{}` has been deleted.".format(pk)},status=204)


class LoginView(APIView):

    def post(self,request):
        correo= request.data['correo']
        contrasenia = request.data['contrasenia']

        user= Empresa.objects.filter(correo=correo).first()
        contra= Empresa.objects.filter(contrasenia=contrasenia).first()
        if user is None:
            raise AuthenticationFailed('User not found!')
            #pa verificar desde el hash
        if contra is None:
            raise AuthenticationFailed('incorrect password')



        #create a jwt
    
        payload={
            'id':user.idempresa,
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


class EmpresaView(APIView):
    
    def get (self,request):

        token= request.COOKIES.get('jwt')

        #decoded to get te user
        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload= jwt.decode(token,'secret',algorithms=['HS256'])
            

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')

        user = Empresa.objects.filter(idempresa=payload['id']).first()

        serializer=EmpresaSerializer(user)

        return Response(serializer.data)

class LogoutView(APIView):

    def post(self,request):
        response= Response()
        response.delete_cookie('jwt')
        response.data={
            'message':'success logout'
        }
        return response