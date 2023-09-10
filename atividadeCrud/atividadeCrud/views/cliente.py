from django.shortcuts import redirect, render, get_object_or_404
from atividadeCrud.models import Clientes
from atividadeCrud.forms import ClienteForm

def home(request):
    cliente = Clientes.objects.all()
    print(cliente)

    return render(request, 'clientes/home.html',{
        'lista_clientes':cliente
    })

def inserir(request):
    frm = ClienteForm(request.POST or None)
    
    if frm.is_valid():
        frm.save()
        return redirect('clientes.home')

    return render(request, 'clientes/form.html', {
        'frm' : frm
    })

def editar(request, id):
    cliente = get_object_or_404(Clientes, pk=id)
    frm = ClienteForm(request.POST or None, instance=cliente)

    if frm.is_valid():
        frm.save()

        return redirect('clientes.home')

    return render(request, 'clientes/form.html', {
        'frm' : frm
        
    })

def excluir(request, id):
    cliente = get_object_or_404(Clientes, pk= id)
    cliente.delete()
    return redirect('clientes.home')