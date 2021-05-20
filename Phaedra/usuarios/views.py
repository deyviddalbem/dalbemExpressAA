from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializer import UsuariosSerializer

# Create your views here.
class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
