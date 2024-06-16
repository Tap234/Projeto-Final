from django.urls import path
from . import views

app_name='doacao'
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('entregas/', views.lista_entregas, name='lista_entregas'),
]