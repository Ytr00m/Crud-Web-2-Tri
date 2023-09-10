from django.shortcuts import redirect, render, get_object_or_404
from atividadeCrud.models import *
from atividadeCrud.forms import *

def home(request):
    itens_de_pedidos = Itens_de_Pedidos.objects.all()
    print(itens_de_pedidos)

    return render(request, 'itens_de_pedidos/home.html',{
        'lista_itens':itens_de_pedidos
    })

def inserir(request):
    frm = ItensForm(request.POST or None)
    
    if frm.is_valid():
        frm.save()
        return redirect('itens_de_pedidos.home')

    return render(request, 'itens_de_pedidos/form.html', {
        'frm' : frm
    })

def editar(request, id):
    itens_de_pedidos = get_object_or_404(Itens_de_Pedidos, pk=id)
    frm = ItensForm(request.POST or None, instance=itens_de_pedidos)

    if frm.is_valid():
        frm.save()

        return redirect('itens_de_pedidos.home')

    return render(request, 'itens_de_pedidos/form.html', {
        'frm' : frm
    })

def excluir(request, id):
    itens_de_pedidos = get_object_or_404(Itens_de_Pedidos, pk= id)
    itens_de_pedidos.delete()
    return redirect('itens_de_pedidos.home')