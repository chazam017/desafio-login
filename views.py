from django.shortcuts import render

# views (views.py)
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistroForm # type: ignore
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail

def registrar(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            send_mail(
                'Bem-vindo!',
                'Você foi registrado com sucesso no desafio técnico da Fidelity!',
                'noreply@meusite.com',
                [usuario.email],
                fail_silently=False,
            )
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'registrar.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        usuario = authenticate(request, email=email, password=senha)
        if usuario:
            login(request, usuario)
            return redirect('menu')
        else:
            messages.error(request, 'Credenciais inválidas.')
    return render(request, 'login.html')

@login_required
def menu(request):
    return render(request, 'menu.html')
