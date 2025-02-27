# forms para validação (forms.py)
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario # type: ignore
import re

class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'email', 'password1', 'password2']

    def clean_first_name(self):
        nome = self.cleaned_data.get('first_name')
        if not nome.isalpha():
            raise forms.ValidationError('O nome deve conter apenas letras.')
        return nome

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if "@" not in email:
            raise forms.ValidationError('Insira um e-mail válido.')
        return email

    def clean_password1(self):
        senha = self.cleaned_data.get('password1')
        if (len(senha) < 8 or not re.search("[A-Z]", senha) or
                not re.search("[0-9]", senha) or not re.search("[@$!%*?&]", senha)):
            raise forms.ValidationError("A senha deve ter pelo menos 8 caracteres, uma letra maiúscula, um número e um caractere especial.")
        return senha