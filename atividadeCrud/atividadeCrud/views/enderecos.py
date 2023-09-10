from django.shortcuts import redirect, render, get_object_or_404
from atividadeCrud.models import *
from atividadeCrud.forms import *

def home(request):
    enderecos = Enderecos.objects.all()
    print(enderecos)

    return render(request, 'enderecos/home.html',{
        'lista_enderecos':enderecos
    })

def inserir(request):
    frm = EnderecoForm(request.POST or None)
    
    if frm.is_valid():
        frm.save()
        return redirect('enderecos.home')

    return render(request, 'enderecos/form.html', {
        'frm' : frm
    })

def editar(request, id):
    enderecos = get_object_or_404(Enderecos, pk=id)
    frm = EnderecoForm(request.POST or None, instance=enderecos)

    if frm.is_valid():
        frm.save()

        return redirect('enderecos.home')

    return render(request, 'enderecos/form.html', {
        'frm' : frm
    })

def excluir(request, id):
    enderecos = get_object_or_404(Enderecos, pk= id)
    enderecos.delete()
    return redirect('enderecos.home')