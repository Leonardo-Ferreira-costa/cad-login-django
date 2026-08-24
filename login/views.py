from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Importa o decorator de métodos HTTP
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        # Busca o usuário pelo e-mail de forma segura
        usuario_objeto = User.objects.filter(email=email).first()

        if usuario_objeto:
            # Tenta autenticar usando o username atrelado ao e-mail encontrado
            user = authenticate(request, username=usuario_objeto.username, password=senha)

            if user is not None:
                login(request, user)  # Cria a sessão do usuário
                return redirect("painel")

            # Caso a autenticação falhe, verifica se o motivo foi conta inativa
            if not usuario_objeto.is_active and usuario_objeto.check_password(senha):
                messages.error(request,"Sua conta ainda não foi ativada. Verifique seu e-mail.")
                return render(request, "login/login.html")

        # Mensagem genérica para evitar User Enumeration
        messages.error(request, "E-mail ou senha inválidos.")

    return render(request, 'login/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')
