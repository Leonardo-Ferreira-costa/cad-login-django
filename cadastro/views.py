from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def cadastro(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        # Validações básicas

        # Verifica se as senhas coincidem
        if senha != confirmar_senha:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'cadastro/cadastro.html')
        
        # Verifica se a senha tem pelo menos 8 caracteres
        if len(senha) < 8:
            messages.error(request, 'A senha deve ter pelo menos 8 caracteres.')
            return render(request, 'cadastro/cadastro.html')
        
        # Verifica se o e-mail já está cadastrado
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email já cadastrado.')
            return render(request, 'cadastro/cadastro.html')

        # Cria o usuário com a senha criptografada (SEMPRE use create_user o django já faz a criptografia da senha)
        user = User.objects.create_user(username=usuario, email=email, password=senha)
        # user.save() #Redundante, pois create_user já salva o usuário no banco de dados, pode ser removido
        

        messages.success(request, 'Cadastro realizado com sucesso! Faça seu login.')
        return redirect('login')

    return render(request, 'cadastro/cadastro.html')