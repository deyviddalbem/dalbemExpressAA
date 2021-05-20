
from django.contrib import admin
from django.urls import path, include
from usuarios.views import UsuariosViewSet
from rest_framework import routers 

router = routers.DefaultRouter()
router.register('usuarios', UsuariosViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
]
