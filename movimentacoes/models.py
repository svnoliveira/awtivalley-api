from django.db import models


class Movimentacao(models.Model):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="movimentacoes"
    )
    produto = models.ForeignKey(
        "produtos.Produto", on_delete=models.CASCADE,
        related_name="movimentacoes"
    )
    quantidade = models.IntegerField(default=1)
    data = models.DateTimeField(auto_now_add=True)
