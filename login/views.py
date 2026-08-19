from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        try:
            # 1. Descobre o username atrelado a esse e-mail
            usuario_objeto = User.objects.get(email=email)
            username_cadastrado = usuario_objeto.username
            
            # 2. Autentica usando o username encontrado, padrão do Django é autenticar pelo username
            user = authenticate(request, username=username_cadastrado, password=senha)
        except User.DoesNotExist:
            # Se o e-mail não existir no banco, define como None para cair no erro
            user = None

        if user is not None:
            login(request, user) # Cria a sessão do usuário
            return redirect('painel')  # Redireciona para a página do painel, atenção para o nome da URL que você definiu no urls.py e não para o caminho do template, pois estamos usando redirect.
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'login/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')
