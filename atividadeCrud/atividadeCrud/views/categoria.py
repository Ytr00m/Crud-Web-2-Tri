from django.shortcuts import redirect, render, get_object_or_404
from atividadeCrud.models import *
from atividadeCrud.forms import *

def home(request):
    categoria = Categorias.objects.all()
    print(categoria)

    return render(request, 'categorias/home.html',{
        'lista_categoria':categoria
    })

def inserir(request):
    frm = CategoriaForm(request.POST or None)
    if frm.is_valid():
        frm.save()
        return redirect('categorias.home')

    return render(request, 'categorias/form.html', {
        'frm' : frm
    })

def editar(request, id):
    categoria = get_object_or_404(Categorias, pk=id)
    frm = CategoriaForm(request.POST or None, instance=categoria)

    if frm.is_valid():
        frm.save()

        return redirect('categorias.home')

    return render(request, 'categorias/form.html', {
        'frm' : frm
    })

def excluir(request, id):
    categoria = get_object_or_404(Categorias, pk= id)
    categoria.delete()
    return redirect('categorias.home')