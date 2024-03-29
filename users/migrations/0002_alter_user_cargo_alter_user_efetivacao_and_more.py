# Generated by Django 5.0.1 on 2024-01-22 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cargo',
            field=models.CharField(blank=True, max_length=127),
        ),
        migrations.AlterField(
            model_name='user',
            name='efetivacao',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='funcao',
            field=models.CharField(blank=True, max_length=127),
        ),
        migrations.AlterField(
            model_name='user',
            name='funcoes_extra',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='observacoes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='setor',
            field=models.CharField(blank=True, max_length=127),
        ),
        migrations.AlterField(
            model_name='user',
            name='ultima_promocao',
            field=models.DateField(blank=True, null=True),
        ),
    ]
