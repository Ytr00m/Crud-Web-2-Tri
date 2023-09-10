from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from atividadeCrud.validators import data_menor_atual, data_menor_igual_atual, numero, EscolhaValidator

class Clientes(models.Model):
    nome_validators = [MinLengthValidator(2, "Nome precisa ter ao menos 2 caracteres."),
                       MaxLengthValidator(100, "Nome pode ter ao máximo 100 caracteres.")]
    datanasc_validators = [data_menor_atual]
    telefone_validators = [numero("Telefone"),
                           MinLengthValidator(8, "Telefone precisa ter ao menos 8 caracteres."),
                           MaxLengthValidator(15, "Telefone pode ter ao máximo 15 caracteres.")]

    nome  = models.CharField(max_length=100, validators=nome_validators)
    email = models.EmailField(max_length=1000, unique=True)
    endereco = models.ForeignKey('Enderecos', on_delete=models.DO_NOTHING, null=True,blank=True, related_name='clientes')
    datanasc = models.DateField(validators=datanasc_validators)
    telefone = models.CharField(max_length=15, validators=telefone_validators) 
    usuario = models.OneToOneField('Usuarios', on_delete=models.SET_NULL, null=True,blank=True, related_name='cliente')

    def __str__(self):
        return self.nome

class Produtos(models.Model):
    nome_validators = [MinLengthValidator(2, "Nome precisa ter ao menos 2 caracteres."),
                       MaxLengthValidator(100, "Nome pode ter ao máximo 100 caracteres.")]
    desc_validators = [MinLengthValidator(10, "Descrição precisa ter ao menos 10 caracteres."),
                       MaxLengthValidator(500, "Descrição pode ter ao máximo 50 caracteres.")]
    preco_validators = [MinValueValidator(0.01, "Preço deve ser maior que 0.")]    
    estoque_validators = [MinValueValidator(0, "Estoque não pode ser menor que 0.")]

    nome = models.CharField(max_length=1000, validators=nome_validators)
    desc = models.CharField(max_length=1000, validators=desc_validators)
    preco = models.DecimalField(max_digits=10, decimal_places=2, validators=preco_validators)
    estoque = models.IntegerField(default=0,null=True, validators=estoque_validators)
    categoria = models.ForeignKey('Categorias', on_delete=models.DO_NOTHING, null=True, related_name='produtos')
    fornecedor = models.ForeignKey('Fornecedores', on_delete=models.DO_NOTHING,null=True,  related_name='produtos', blank=True)

    def __str__(self):
        return self.nome

class Pedidos(models.Model):
    data_validators = [data_menor_igual_atual]
    data_entrega_real_validators = [data_menor_igual_atual]
    status_validators = [EscolhaValidator(["Em aberto", "Em andamento", "Finalizado"])]
    valor_total_validators = [MinValueValidator(0.01, "Valor deve ser maior que 0.")]

    data = models.DateField(null=True, blank=True)
    data_entrega_prev = models.DateField()
    data_entrega_real = models.DateField(null=True, blank=True, validators=data_entrega_real_validators)
    status = models.CharField(max_length=20, validators=status_validators)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, validators=valor_total_validators)
    cliente = models.ForeignKey('Clientes', on_delete=models.DO_NOTHING, related_name='pedidos')
    pagamento = models.ForeignKey('Pagamentos', on_delete=models.DO_NOTHING, null=True, related_name='pedidos', blank=True)

    def __str__(self):
        return f"{self.data}, R${self.valor_total}"


class Categorias(models.Model):
    nome_validadors = [MinLengthValidator(2, "Nome precisa ter ao menos 2 caracteres."),
                       MaxLengthValidator(50, "Nome pode ter ao máximo 50 caracteres.")]
    
    desc_validators = [MinLengthValidator(10, "Descrição precisa ter ao menos 10 caracteres."),
                       MaxLengthValidator(500, "Descrição pode ter ao máximo 50 caracteres.")]
    
    nome  = models.CharField(max_length=100, validators=nome_validadors)
    desc = models.CharField(max_length=500, validators=desc_validators)

    def __str__(self):
        return self.nome

class Fornecedores(models.Model):
    nome_validators = [MinLengthValidator(2, "Nome precisa ter ao menos 2 caracteres."),
                       MaxLengthValidator(100, "Nome pode ter ao máximo 100 caracteres.")] 
    endereco_validators = [MinLengthValidator(5, "Endereço precisa ter ao menos 5 caracteres."),
                       MaxLengthValidator(200, "Endereço pode ter ao máximo 200 caracteres.")]
    telefone_validators = [numero("Telefone"),
                           MinLengthValidator(8, "Telefone precisa ter ao menos 8 caracteres."),
                           MaxLengthValidator(15, "Telefone pode ter ao máximo 100 caracteres.")]   

    nome = models.CharField(max_length=100, validators=nome_validators)
    endereco = models.CharField(max_length=200)
    email = models.EmailField(unique=True, validators=endereco_validators)
    telefone = models.CharField(max_length=15, validators=telefone_validators)

    def __str__(self):
        return self.nome

class Funcionarios(models.Model):
    nome_validators = [MinLengthValidator(2, "Nome precisa ter ao menos 2 caracteres."),
                       MaxLengthValidator(100, "Nome pode ter ao máximo 100 caracteres.")] 
    cargo_validators = [MinLengthValidator(2, "Cargo precisa ter ao menos 2 caracteres."),
                       MaxLengthValidator(50, "Cargo pode ter ao máximo 50 caracteres.")]
    telefone_validators = [numero("Telefone"),
                           MinLengthValidator(8, "Telefone precisa ter ao menos 8 caracteres."),
                           MaxLengthValidator(15, "Telefone pode ter ao máximo 100 caracteres.")]
    
    nome = models.CharField(max_length=100, validators=nome_validators)
    cargo = models.CharField(max_length=20, validators=cargo_validators)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, validators=telefone_validators)

    def __str__(self) -> str:
        return f"{self.nome}, {self.cargo}"
    
class Usuarios(models.Model):
    nome_validators = [MinLengthValidator(2, "Nome precisa ter ao menos 2 caracteres."),
                       MaxLengthValidator(100, "Nome pode ter ao máximo 100 caracteres.")]
    
    senha_validators = [MinLengthValidator(8, "Senha precisa ter ao menos 8 caracteres."),
                           MaxLengthValidator(50, "Senha pode ter ao máximo 50 caracteres.")]



    nome = models.CharField(max_length=100, validators=nome_validators)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=20, validators=senha_validators)

    def __str__(self):
        return self.nome

class Enderecos(models.Model):
    rua_validators = [MinLengthValidator(2, "Rua precisa ter ao menos 2 caracteres."),
                      MaxLengthValidator(100, "Rua pode ter ao máximo 100 caracteres.")]
    
    numero_validators = [numero("Número"),
                         MaxLengthValidator(10, "Número precisa ter no máximo 10 caracteres.")]
    
    bairro_validators = [MinLengthValidator(2, "Bairro precisa ter ao menos 2 caracteres."),
                      MaxLengthValidator(50, "Bairro pode ter ao máximo 50 caracteres.")]
    
    cidade_validators = [MinLengthValidator(2, "Cidade precisa ter ao menos 2 caracteres."),
                      MaxLengthValidator(50, "Cidade pode ter ao máximo 50 caracteres.")]

    estado_validators = [MinLengthValidator(2, "Estado precisa ter 2 caracteres.")]

    cep_validators = [numero("Cep"),
                      MinLengthValidator(8, "Cep precisa ter 8 caracteres.")]

    rua = models.CharField(max_length=100, validators=rua_validators)
    numero = models.CharField(max_length=10, validators=numero_validators)
    complemento = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50, validators=bairro_validators)
    cidade = models.CharField(max_length=50, validators=cidade_validators)
    estado = models.CharField(max_length=2, validators=estado_validators)
    cep = models.CharField(max_length=8, validators=cep_validators)

    def __str__(self) -> str:
        return f"{self.rua}, n°{self.numero}"

class Pagamentos(models.Model):
    tipo_validators = [EscolhaValidator(["Cartão de crédito", "Boleto", "Transferência bancária"])]
    valor_validators = [MinValueValidator(0.01, "Valor deve ser maior que 0.")]
    data_validators = [data_menor_atual]

    tipo = models.CharField(max_length=50, validators=tipo_validators)
    valor = models.DecimalField(max_digits=10, decimal_places=2, validators=valor_validators)
    data = models.DateField(validators=data_validators)

    def __str__(self) -> str:
        return f"{self.tipo}, R${self.valor}"
    
class Compras(models.Model):
    quantidade_validators = [MinValueValidator(1, "Quantidade deve ser maior que 0.")]
    preco_validators = [MinValueValidator(1*10**-2, "Preço deve ser maior que 0.")]

    produto = models.IntegerField()
    quantidade = models.IntegerField(validators=quantidade_validators)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2, validators=preco_validators)
    data_compra = models.DateTimeField(auto_now_add=True)
    comprador = models.ForeignKey("Clientes", on_delete=models.SET_NULL, null=True, related_name='compras')

class Itens_de_Pedidos(models.Model):
    pedido = models.ForeignKey('Pedidos', on_delete=models.CASCADE, related_name='itensPedidos')
    produto = models.ForeignKey('Produtos', on_delete=models.DO_NOTHING, related_name='pedidos')
    quantidade = models.IntegerField()





