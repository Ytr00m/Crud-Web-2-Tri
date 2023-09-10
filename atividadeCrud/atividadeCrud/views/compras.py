from django.shortcuts import redirect, render, get_object_or_404
from atividadeCrud.models import *
from atividadeCrud.forms import *

def home(request):
    compras = Compras.objects.all()
    print(compras)

    return render(request, 'compras/home.html',{
        'lista_compras':compras
    })

def inserir(request):
    frm = CompraForm(request.POST or None)
    
    if frm.is_valid():
        frm.save()
        return redirect('compras.home')

    return render(request, 'compras/form.html', {
        'frm' : frm
    })

def editar(request, id):
    compras = get_object_or_404(Compras, pk=id)
    frm = CompraForm(request.POST or None, instance=compras)

    if frm.is_valid():
        frm.save()

        return redirect('compras.home')

    return render(request, 'compras/form.html', {
        'frm' : frm
    })

def excluir(request, id):
    compras = get_object_or_404(Compras, pk= id)
    compras.delete()
    return redirect('compras.home')