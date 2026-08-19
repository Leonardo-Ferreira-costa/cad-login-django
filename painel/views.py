from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as Usuario

@login_required(login_url='login')
def painel_principal(request):
    usuarios = {
         'usuarios': Usuario.objects.all()
    }
    return render(request, 'painel/home.html', usuarios)

# Create your views here.
