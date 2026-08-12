from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        # Autentica o usuário no banco de dados
        user = authenticate(request, username=usuario, password=senha)

        if user is not None:
            login(request, user) # Cria a sessão do usuário
            return redirect('painel')  # Redireciona para a página do painel
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'login/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')
