from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth import login as login_django


def login(request):
    if request.method == "GET":
        return render(request, 'usuarios/login.html')
    else:
        username = request.POST.get('email')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)
            return HttpResponse('Sucesso!')
        else:
            return HttpResponse('Credenciais inválidas!')

def cadastro(request):
    return render(request, 'usuarios/cadastro.html')

def home(request):
    return render(request, 'usuarios/home.html')

def fretista(request):
    return render(request, 'usuarios/fretista.html')

def conversas(request):
    return render(request, 'usuarios/conversas.html')

def enderecos(request):
    return render(request, 'usuarios/enderecos.html')

def dados_da_conta(request):
    return render(request, 'usuarios/dados_da_conta.html')

def meus_agendamentos(request):
    return render(request, 'usuarios/meus_agendamentos.html')

def configuracoes(request):
    return render(request, 'usuarios/configuracoes.html')

def seguranca(request):
    return render(request, 'usuarios/seguranca.html')

def logout_view(request):
    return render(request, 'usuarios/logout.html')
