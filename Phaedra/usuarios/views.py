from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializer import UsuariosSerializer

# Create your views here.
class UsuariosListViewSet(viewsets.ModelViewSet):
    queryset =  Usuarios.objects.all()
    serializer_class = UsuariosSerializer
    
class UsuariosListIdViewSet(viewsets.ModelViewSet):
    queryset =  Usuarios.objects.filter()
    serializer_class = UsuariosSerializer
