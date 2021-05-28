from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.urls.resolvers import URLPattern
from django.views.generic.base import TemplateView
from . import views



urlpatterns = [
   path('lista_usuarios_all/', views.lista_usuarios_all, name="lista_usuarios_all"), 
   path('meus_dados/',views.mostrar_MeusDados, name="meusDadosUsuario"),
   path('cadastrar_foto/',views.cadastrar_foto_usuario, name="inserir_foto"),
   path('atualizar_Meus_Dados/<int:pk>', views.Atualizar_Cadastro_usuario.as_view(), name='atualizar_Cadastro_usuario'),
]