from django.db import models


class Produto(models.Model):
    imagem = models.CharField(max_length=255)
    nome = models.CharField(max_length=127, unique=True)
    categoria = models.CharField(max_length=127)
    preco = models.FloatField(default=9999)
    estoque = models.IntegerField(default=0)
    qtdCondicao = models.IntegerField(default=0)
    # movimentacoes 1tm
