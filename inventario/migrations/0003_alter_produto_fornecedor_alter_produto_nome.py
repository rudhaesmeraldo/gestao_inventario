# Generated by Django 5.1.7 on 2025-03-14 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_alter_produto_fornecedor_alter_produto_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='fornecedor',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='nome',
            field=models.CharField(max_length=250),
        ),
    ]
