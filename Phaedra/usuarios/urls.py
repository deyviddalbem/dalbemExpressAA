from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.urls.resolvers import URLPattern
from django.views.generic.base import TemplateView
from . import views

app_name = 'usuarios'

urlpatterns = [
   path('lista_usuarios_all/', views.lista_usuarios_all, name="lista_usuarios_all"), 
]