from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FotoUsuarios(models.Model):
    foto_usuarios = models.FileField(upload_to='media/%Y/%m/%d/')
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='NOME DO USUARIO')
    
    class Meta:
        verbose_name = "fotos_Usuario"
        verbose_name_plural = "fotos_Usuario"