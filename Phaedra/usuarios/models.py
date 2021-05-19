from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nome_usuario = models.CharField('NOME USUARIO', max_length=30)
    sobrenome_usuario = models.CharField('SOBRENOME USUARIO', max_length=30)
    username = models.CharField('USERNAME', max_length=30)
    senha_usuario = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nome_usuario + self.sobrenome_usuario + self.username