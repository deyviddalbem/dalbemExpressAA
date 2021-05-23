from django.db.models import fields
from rest_framework import serializers 
from django.contrib.auth.models import User
from .models import *

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','last_name', 'username']
