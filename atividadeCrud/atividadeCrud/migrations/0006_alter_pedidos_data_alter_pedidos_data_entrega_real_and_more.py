# Generated by Django 4.2.5 on 2023-09-10 00:57

import atividadeCrud.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atividadeCrud', '0005_alter_pagamentos_data_alter_pagamentos_tipo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='data',
            field=models.DateTimeField(validators=[atividadeCrud.validators.data_menor_igual_atual]),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='data_entrega_real',
            field=models.DateField(blank=True, null=True, validators=[atividadeCrud.validators.data_menor_igual_atual]),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='status',
            field=models.CharField(max_length=20, validators=[atividadeCrud.validators.EscolhaValidator(['Em aberto', 'Em andamento', 'Finalizado'])]),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='valor_total',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.01, 'Valor deve ser maior que 0.')]),
        ),
    ]
