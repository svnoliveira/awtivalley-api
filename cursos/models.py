from django.db import models


class Curso(models.Model):
    nome = models.CharField(max_length=127, unique=True)
    validade = models.IntegerField(default=0)
    # users
