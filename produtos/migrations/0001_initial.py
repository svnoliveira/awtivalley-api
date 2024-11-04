# Generated by Django 5.0.1 on 2024-11-02 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.CharField(max_length=255)),
                ('nome', models.CharField(max_length=127, unique=True)),
                ('categoria', models.CharField(max_length=127)),
                ('preco', models.FloatField(default=9999)),
                ('estoque', models.IntegerField(default=0)),
                ('qtdCondicao', models.IntegerField(default=0)),
            ],
        ),
    ]