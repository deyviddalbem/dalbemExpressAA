from django.contrib import admin
from .models import FotoUsuarios

# Register your models here.
class FotosusuariosAdmin(admin.ModelAdmin):
    list_display = ('id', 'foto_usuarios')
    list_display_links = ('id',)
    
admin.site.register(FotoUsuarios,FotosusuariosAdmin)