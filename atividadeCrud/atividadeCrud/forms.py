from typing import Any
from atividadeCrud.models import *
from django.forms import ModelForm
from datetime import datetime

class ClienteForm(ModelForm):
    class Meta:
        model = Clientes
        fields ='__all__'

class ProdutoForm(ModelForm):
    class Meta:
        model = Produtos
        fields ='__all__'

class CategoriaForm(ModelForm):
    class Meta:
        model = Categorias
        fields ='__all__'
        
class PedidosForm(ModelForm):
    class Meta:
        model = Pedidos
        fields ='__all__'

    def clean(self):
        dados = super().clean()
        print(dados)
        data_pedido = dados['data']
        entrega_prev = dados['data_entrega_prev']
        entrega_real = dados['data_entrega_real']

        if (entrega_prev - data_pedido).days <= 0:
            self.add_error('data_entrega_prev', "Data de Entrega Prevista deve ser posterior a data do Pedido.")

        if (entrega_real - data_pedido).days <= 0:
            self.add_error('data_entrega_real', "Data de Entrega Real deve ser posterior a data do Pedido.")
        
        return dados

class FornecedorForm(ModelForm):
    class Meta:
        model = Fornecedores
        fields ='__all__'

class FuncionarioForm(ModelForm):
    class Meta:
        model = Funcionarios
        fields ='__all__'

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuarios
        fields ='__all__'

class EnderecoForm(ModelForm):
    class Meta:
        model = Enderecos
        fields ='__all__'

class PagamentoForm(ModelForm):
    class Meta:
        model = Pagamentos
        fields ='__all__'

class CompraForm(ModelForm):
    class Meta:
        model = Compras
        fields ='__all__'

class ItensForm(ModelForm):
    class Meta:
        model = Itens_de_Pedidos
        fields ='__all__'