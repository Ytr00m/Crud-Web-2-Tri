"""atividadeCrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from atividadeCrud.views import cliente,produto,pedidos,categoria, fornecedores,funcionarios,compras,enderecos,usuarios,pagamentos,itenspedidos

urlpatterns = [
    path('clientes', cliente.home, name="clientes.home"),
    path('clientes/inserir', cliente.inserir, name="clientes.inserir"),
    path('clientes/editar/<id>', cliente.editar, name="clientes.editar"),
    path('clientes/excluir/<id>', cliente.excluir, name="clientes.excluir"),
    
    path('produto', produto.home, name="produtos.home"),
    path('produto/inserir', produto.inserir, name="produtos.inserir"),
    path('produto/editar/<id>', produto.editar, name="produtos.editar"),
    path('produto/excluir/<id>', produto.excluir, name="produtos.excluir"),
    
    path('pedidos', pedidos.home, name="pedidos.home"),
    path('pedidos/inserir', pedidos.inserir, name="pedidos.inserir"),
    path('pedidos/editar/<id>', pedidos.editar, name="pedidos.editar"),
    path('pedidos/excluir/<id>', pedidos.excluir, name="pedidos.excluir"),
    
    path('categoria', categoria.home, name="categorias.home"),
    path('categoria/inserir', categoria.inserir, name="categorias.inserir"),
    path('categoria/editar/<id>', categoria.editar, name="categorias.editar"),
    path('categoria/excluir/<id>', categoria.excluir, name="categorias.excluir"),
    
    path('fornecedor', fornecedores.home, name="fornecedores.home"),
    path('fornecedor/inserir', fornecedores.inserir, name="fornecedores.inserir"),
    path('fornecedor/editar/<id>', fornecedores.editar, name="fornecedores.editar"),
    path('fornecedor/excluir/<id>', fornecedores.excluir, name="fornecedores.excluir"),
    
    path('funcionarios', funcionarios.home, name="funcionarios.home"),
    path('funcionarios/inserir', funcionarios.inserir, name="funcionarios.inserir"),
    path('funcionarios/editar/<id>', funcionarios.editar, name="funcionarios.editar"),
    path('funcionarios/excluir/<id>', funcionarios.excluir, name="funcionarios.excluir"),

    path('usuarios', usuarios.home, name="usuarios.home"),
    path('usuarios/inserir', usuarios.inserir, name="usuarios.inserir"),
    path('usuarios/editar/<id>', usuarios.editar, name="usuarios.editar"),
    path('usuarios/excluir/<id>', usuarios.excluir, name="usuarios.excluir"),

    path('enderecos', enderecos.home, name="enderecos.home"),
    path('enderecos/inserir', enderecos.inserir, name="enderecos.inserir"),
    path('enderecos/editar/<id>', enderecos.editar, name="enderecos.editar"),
    path('enderecos/excluir/<id>', enderecos.excluir, name="enderecos.excluir"),

    path('pagamentos', pagamentos.home, name="pagamentos.home"),
    path('pagamentos/inserir', pagamentos.inserir, name="pagamentos.inserir"),
    path('pagamentos/editar/<id>', pagamentos.editar, name="pagamentos.editar"),
    path('pagamentos/excluir/<id>', pagamentos.excluir, name="pagamentos.excluir"),

    path('compras', compras.home, name="compras.home"),
    path('compras/inserir', compras.inserir, name="compras.inserir"),
    path('compras/editar/<id>', compras.editar, name="compras.editar"),
    path('compras/excluir/<id>', compras.excluir, name="compras.excluir"),

    path('itenspedidos', itenspedidos.home, name="itens_de_pedidos.home"),
    path('itenspedidos/inserir', itenspedidos.inserir, name="itens_de_pedidos.inserir"),
    path('itenspedidos/editar/<id>', itenspedidos.editar, name="itens_de_pedidos.editar"),
    path('itenspedidos/excluir/<id>', itenspedidos.excluir, name="itens_de_pedidos.excluir"),
]
