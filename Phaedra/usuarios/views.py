from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializer import UsuariosSerializer
from django.contrib.auth.models import User

# Create your views here.
class UsuariosListViewSet(viewsets.ModelViewSet):
    queryset =  User.objects.all()
    serializer_class = UsuariosSerializer
    
class UsuariosListIdViewSet(viewsets.ModelViewSet):
    queryset =  User.objects.filter()
    serializer_class = UsuariosSerializer

def lista_usuarios_all(request):
    return render(request, 'usuarios/lista_usuarios.html')