from django.shortcuts import render, redirect, HttpResponse

from .models import Produto
from .forms import ProdutoForm






def produtos(request):
    dados = {
        'dados':Produto.objects.all()
    }
    return render(request,'investimentos/produtos.html', context=dados)

def detalhe(request, id_produto):
    dados = {
        'dados': Produto.objects.get(pk=id_produto)
    }
    return render(request,'investimentos/detalhe.html',dados)

def criar(request):
    if request.method == 'POST':
        produto_form = ProdutoForm(request.POST)
        if produto_form.is_valid():
            produto_form.save()
        return redirect('produtos')
    else:
        produto_form = ProdutoForm()
        formulario = {
            'formulario': produto_form
        }
    return render(request, 'investimentos/novo_produto.html', context=formulario)

def editar(request, id_produto):
    produto = Produto.objects.get(pk=id_produto)
    # novo_produto/1 -. GET
    if request.method == 'GET':
        formulario = ProdutoForm(instance=produto)
        return render(request, 'investimentos/novo_produto.html', {'formulario': formulario})
    #caso sela requisiçao seja POST
    else:
        formulario = ProdutoForm(request.POST, instance=produto)
        if formulario.is_valid():
            formulario.save()
        return redirect('produtos')
    
def excluir(request, id_produto):
        produto = Produto.objects.get(pk=id_produto)
        if request.method == 'POST':
            produto.delete()
            return redirect('produtos')
        return render(request, 'investimentos/confirmar_exclusao.html',{'item':produto})

