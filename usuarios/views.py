from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django

######## Pagino de login, ta dando erro essa bosta ########
def login(request):
    if request.method == "GET":
        return render(request, 'usuarios/login.html')
    else:
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = authenticate(request, username=email.useremail, password=senha) ######## erro

        if user:
            login_django(request, user)
            return HttpResponse('Sucesso!')
        else:
            return HttpResponse('Credenciais inválidas!')


######## Pagina de cadastro ########
def cadastro(request):
    if request.method == "GET":
        return render(request, 'usuarios/cadastro.html')
    else:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.create_user(username=nome, email=email, password=senha)

        if user:
            login_django(request, user)
            return HttpResponse('Cadastrado com sucesso!')
        else:
            return HttpResponse('Conta já existente!')
    

######## pagina inicial ########
def home(request):
    return render(request, 'usuarios/home.html')