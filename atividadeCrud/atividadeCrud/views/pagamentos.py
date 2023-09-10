from django.shortcuts import redirect, render, get_object_or_404
from atividadeCrud.models import *
from atividadeCrud.forms import *

def home(request):
    pagamento = Pagamentos.objects.all()
    print(pagamento)

    return render(request, 'pagamentos/home.html',{
        'lista_pagamentos':pagamento
    })

def inserir(request):
    frm = PagamentoForm(request.POST or None)
    
    if frm.is_valid():
        frm.save()
        return redirect('pagamentos.home')

    return render(request, 'pagamentos/form.html', {
        'frm' : frm
    })

def editar(request, id):
    pagamento = get_object_or_404(Pagamentos, pk=id)
    frm = PagamentoForm(request.POST or None, instance=pagamento)

    if frm.is_valid():
        frm.save()

        return redirect('pagamentos.home')

    return render(request, 'pagamentos/form.html', {
        'frm' : frm
    })

def excluir(request, id):
    pagamento = get_object_or_404(Pagamentos, pk= id)
    pagamento.delete()
    return redirect('pagamentos.home')