from django.shortcuts import redirect, render, get_object_or_404
from atividadeCrud.models import *
from atividadeCrud.forms import *

def home(request):
    funcionarios = Funcionarios.objects.all()
    print(funcionarios)

    return render(request, 'funcionarios/home.html',{
        'lista_funcionarios':funcionarios
    })

def inserir(request):
    frm = FuncionarioForm(request.POST or None)
    
    if frm.is_valid():
        frm.save()
        return redirect('funcionarios.home')

    return render(request, 'funcionarios/form.html', {
        'frm' : frm
    })

def editar(request, id):
    funcionarios = get_object_or_404(Funcionarios, pk=id)
    frm = FuncionarioForm(request.POST or None, instance=funcionarios)

    if frm.is_valid():
        frm.save()

        return redirect('funcionarios.home')

    return render(request, 'funcionarios/form.html', {
        'frm' : frm
    })

def excluir(request, id):
    funcionarios = get_object_or_404(Funcionarios, pk= id)
    funcionarios.delete()
    return redirect('funcionarios.home')