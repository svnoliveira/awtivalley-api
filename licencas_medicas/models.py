from django.db import models


class Licenca_medica(models.Model):
    ciclo = models.CharField(max_length=127)
    data = models.DateField()
    responsavel = models.CharField(max_length=127)
    crm = models.CharField(max_length=127)
    # user
