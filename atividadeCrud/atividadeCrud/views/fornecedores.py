from django.shortcuts import redirect, render, get_object_or_404
from atividadeCrud.models import *
from atividadeCrud.forms import *

def home(request):
    fornecedores = Fornecedores.objects.all()
    print(fornecedores)

    return render(request, 'fornecedores/home.html',{
        'lista_fornecedores':fornecedores
    })

def inserir(request):
    frm = FornecedorForm(request.POST or None)
    if frm.is_valid():
        frm.save()
        return redirect('fornecedores.home')

    return render(request, 'fornecedores/form.html', {
        'frm' : frm
    })

def editar(request, id):
    fornecedores = get_object_or_404(Fornecedores, pk=id)
    frm = FornecedorForm(request.POST or None, instance=fornecedores)

    if frm.is_valid():
        frm.save()

        return redirect('fornecedores.home')

    return render(request, 'fornecedores/form.html', {
        'frm' : frm
    })

def excluir(request, id):
    fornecedores = get_object_or_404(Fornecedores, pk= id)
    fornecedores.delete()
    return redirect('fornecedores.home')