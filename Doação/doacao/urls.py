from django.urls import path
from . import views

app_name = 'doacao'  # Certifique-se de definir o app_name

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('produtos/aumentar/', views.lista_produtos, {'acao': 'aumentar'}, name='lista_produtos_aumentar'),
    path('produtos/diminuir/', views.lista_produtos, {'acao': 'diminuir'}, name='lista_produtos_diminuir'),
]
