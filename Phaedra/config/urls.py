
from django.contrib import admin
from django.urls import path, include
from usuarios.views import UsuariosListViewSet, UsuariosListIdViewSet
from rest_framework import routers 

router = routers.DefaultRouter()
router.register('usuarios/all', UsuariosListViewSet)
router.register('usuarios/filtro', UsuariosListIdViewSet)

urlpatterns = [
    #path('usuarios/', include('usuarios.urls')),
    path('api/',include(router.urls)),
    path('admin/', admin.site.urls),
]
