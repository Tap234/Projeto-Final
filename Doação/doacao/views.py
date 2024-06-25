from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Produto, Doacao, DoacaoItem, Entrega, Entrega_Item
from django.urls import reverse

def inicio(request):
    return render(request, 'inicio.html')

def lista_produtos(request, acao):
    if request.method == 'POST':
        for produto in Produto.objects.all():
            quantidade = request.POST.get(f'quantidade_{produto.id}', None)
            if quantidade:
                quantidade = int(quantidade)
                if acao == 'aumentar' and quantidade > 0:
                    produto.incrementar_quantidade(quantidade)
                elif acao == 'diminuir' and quantidade < 0:
                    if produto.quantidade >= abs(quantidade):
                        produto.decrementar_quantidade(abs(quantidade))
        return redirect('doacao:inicio')  # Redireciona para a mesma página após a atualização

    produtos = Produto.objects.all()
    return render(request, 'lista_produtos.html', {'produtos': produtos, 'acao': acao})
