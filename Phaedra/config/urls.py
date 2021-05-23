
from django.contrib import admin
from django.urls import path, include, re_path
from usuarios.views import UsuariosListViewSet, UsuariosListIdViewSet
from rest_framework import routers 
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView


router = routers.DefaultRouter()
router.register('usuarios/all', UsuariosListViewSet)
router.register('usuarios/filtro', UsuariosListIdViewSet)

urlpatterns = [
    path('usuarios/', include('usuarios.urls')),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('template.urls')),
    
]
