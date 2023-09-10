from django.shortcuts import redirect, render, get_object_or_404
from atividadeCrud.models import *
from atividadeCrud.forms import *

def home(request):
    usuarios = Usuarios.objects.all()
    print(usuarios)

    return render(request, 'usuarios/home.html',{
        'lista_usuarios':usuarios
    })

def inserir(request):
    frm = UsuarioForm(request.POST or None)
    
    if frm.is_valid():
        frm.save()
        return redirect('usuarios.home')

    return render(request, 'usuarios/form.html', {
        'frm' : frm
    })

def editar(request, id):
    usuarios = get_object_or_404(Usuarios, pk=id)
    frm = UsuarioForm(request.POST or None, instance=usuarios)

    if frm.is_valid():
        frm.save()

        return redirect('usuarios.home')

    return render(request, 'usuarios/form.html', {
        'frm' : frm
    })

def excluir(request, id):
    usuarios = get_object_or_404(Usuarios, pk= id)
    usuarios.delete()
    return redirect('usuarios.home')