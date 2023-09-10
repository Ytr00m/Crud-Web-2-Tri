# Generated by Django 4.2.5 on 2023-09-09 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atividadeCrud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='compras',
            name='comprador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='compras', to='atividadeCrud.clientes'),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='pagamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='pedidos', to='atividadeCrud.pagamentos'),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='produtos', to='atividadeCrud.categorias'),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='fornecedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='produtos', to='atividadeCrud.fornecedores'),
        ),
    ]