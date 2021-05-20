from django.db.models import fields
from rest_framework import serializers 
from .models import *

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ['id', 'nome_usuario', 'sobrenome_usuario', 'username']
