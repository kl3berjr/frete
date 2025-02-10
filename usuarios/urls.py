from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('fretista/', views.fretista, name='fretista'),
    path('conversas/', views.conversas, name='conversas'),
    path('enderecos/', views.enderecos, name='enderecos'),
    path('dados-da-conta/', views.dados_da_conta, name='dados_da_conta'),
    path('meus-agendamentos/', views.meus_agendamentos, name='meus_agendamentos'),
    path('configuracoes/', views.configuracoes, name='configuracoes'),
    path('seguranca/', views.seguranca, name='seguranca'),
    path('logout/', views.logout_view, name='logout'),
]
