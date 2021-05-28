from .models import FotoUsuarios
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PessoaUserFormUpdate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PessoaUserFormUpdate, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs = {
            'class': 'form-group form-control', 'type': 'text', 'placeholder': 'Nome'}
        self.fields['last_name'].widget.attrs = {
            'class': 'form-group form-control', 'type': 'text', 'placeholder': 'Sobrenome'}
        self.fields['email'].widget.attrs = {
            'class': 'form-group form-control', 'type': 'mail', 'placeholder': 'E-mail'}
        self.fields['username'].widget.attrs = {
            'class': 'form-group form-control', 'type': 'mail', 'placeholder': 'username'}

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
        
class CadastroFotoUsuarioForm(forms.ModelForm):
    class Meta:
        model = FotoUsuarios
        fields = '__all__'
