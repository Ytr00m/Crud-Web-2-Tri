from django.shortcuts import redirect, render, get_object_or_404
from atividadeCrud.models import *
from atividadeCrud.forms import *
from django.http import HttpRequest

def home(request):
    pedidos = Pedidos.objects.all()
    print(pedidos)

    return render(request, 'pedidos/home.html',{
        'lista_pedidos':pedidos
    })

def inserir(request):
    frm = PedidosForm(request.POST or None)
    
    if frm.is_valid():
        frm.save()
        return redirect('pedidos.home')

    return render(request, 'pedidos/form.html', {
        'frm' : frm
    })

def editar(request: HttpRequest, id):
    pedidos = get_object_or_404(Pedidos, pk=id)
    frm = PedidosForm(request.POST or None, instance=pedidos)

    if frm.is_valid():
        frm.save()

        return redirect('pedidos.home')

    return render(request, 'pedidos/form.html', {
        'frm' : frm
    })

def excluir(request, id):
    pedidos = get_object_or_404(Clientes, pk= id)
    pedidos.delete()
    return redirect('pedidos.home')