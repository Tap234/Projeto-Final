from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Produto, Doacao, DoacaoItem, Entrega, Entrega_Item
from django.urls import reverse

def inicio(request):
    return render(request, 'inicio.html')

def lista_produtos(request):
    if request.method == 'POST':
        produto_id = request.POST.get('produto_id')
        quantidade = int(request.POST.get('quantidade', 0))
        produto = get_object_or_404(Produto, id=produto_id)
        produto.incrementar_quantidade(quantidade)
        return redirect('doacao:inicio')# Redireciona para a lista de produtos após incrementar

    produtos = Produto.objects.all()
    return render(request, 'lista_produtos.html', {'produtos': produtos})



def lista_entregas(request):
    if request.method == 'POST':
        produto_id = request.POST.get('produto_id')
        quantidade = int(request.POST.get('quantidade', 0))
        produto = get_object_or_404(Produto, id=produto_id)
        produto.decrementar_quantidade(quantidade)
        return redirect('doacao:inicio')  # Redireciona para a lista de produtos após incrementar

    produtos = Produto.objects.all()
    return render(request, 'lista_produtos.html', {'produtos': produtos})