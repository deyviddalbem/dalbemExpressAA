from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from django.urls import reverse_lazy
from .serializer import UsuariosSerializer
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import *

# Create your views here.
class UsuariosListViewSet(viewsets.ModelViewSet):
    queryset =  User.objects.all()
    serializer_class = UsuariosSerializer
    
class UsuariosListIdViewSet(viewsets.ModelViewSet):
    queryset =  User.objects.filter()
    serializer_class = UsuariosSerializer

def lista_usuarios_all(request):
    return render(request, 'usuarios/lista_usuarios.html')

##### Função para mostrar os dados do usuário que está autenticado no momento
@login_required()
def mostrar_MeusDados(request):
    mostrar_foto_usuario = FotoUsuarios.objects.filter(id=request.user.id)
    dadosUsuario = User.objects.filter(id=request.user.id)
    context = {'dadosUsuario': dadosUsuario, 'mostrar_foto_usuario': mostrar_foto_usuario}
    return render(request, 'usuarios/meus_dados_usuario.html', context)

class Atualizar_Cadastro_usuario(UpdateView):
    model = User
    form_class = PessoaUserFormUpdate
    template_name = "usuarios/atualizar_meus_dados_usuario.html"
    success_url = reverse_lazy('meusDadosUsuario')
    