from django.db import models


class Registro_de_ponto(models.Model):
    entrada = models.DateTimeField()
    saida = models.DateTimeField()
    horas = models.TimeField()
    justificativa = models.TextField(blank=True)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE,
        related_name="registros_de_ponto"
    )
