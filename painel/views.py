from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def painel_principal(request):
    return render(request, 'painel/home.html')

# Create your views here.
