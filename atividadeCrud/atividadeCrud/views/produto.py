from django.shortcuts import redirect, render, get_object_or_404
from atividadeCrud.models import *
from atividadeCrud.forms import *

def home(request):
    produtos = Produtos.objects.all()

    return render(request, 'produtos/home.html',{
        'lista_produtos':produtos
    })

def inserir(request):
    frm = ProdutoForm(request.POST or None)
    
    if frm.is_valid():
        frm.save()

        return redirect('produtos.home')

    return render(request, 'produtos/form.html', {
        'frm' : frm
    })

def editar(request, id):
    produto = get_object_or_404(Produtos, pk=id)
    frm = ProdutoForm(request.POST or None, instance=produto)

    if frm.is_valid():
        frm.save()

        return redirect('produtos.home')

    return render(request, 'produtos/form.html', {
        'frm' : frm
    })

def excluir(request, id):
    produto = get_object_or_404(Produtos, pk= id)
    produto.delete()
    return redirect('produtos.home')