from django.contrib import admin
from .models import Usuarios

# Register your models here.
class usuariosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_usuario', 'sobrenome_usuario', 'username')
    list_display_links = ('id', 'nome_usuario', 'username')
    search_fields = ('nome', 'username',)
    
admin.site.register(Usuarios,usuariosAdmin)