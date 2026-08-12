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
        if senha != confirmar_senha:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'cadastro.html')

        if User.objects.filter(username=usuario).exists():
            messages.error(request, 'Nome de usuário já cadastrado.')
            return render(request, 'cadastro.html')

        # Cria o usuário com a senha criptografada (SEMPRE use create_user)
        user = User.objects.create_user(username=usuario, email=email, password=senha)
        user.save()

        messages.success(request, 'Cadastro realizado com sucesso! Faça seu login.')
        return redirect('login')

    return render(request, 'cadastro/cadastro.html')