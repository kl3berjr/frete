from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django


def login(request):
    if request.method == "GET":
        return render(request, 'usuarios/login.html')
    else:
        username = request.POST.get('name')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)
            return render(request, 'usuarios/fretista.html')
        else:
            return HttpResponse('Credenciais inválidas!')

def cadastro(request):
    return render(request, 'usuarios/cadastro.html')

def home(request):
    return render(request, 'usuarios/home.html')

def perfil(request):
    return render(request, 'usuarios/perfil.html')

def fretista(request):
    return render(request, 'usuarios/fretista.html')


