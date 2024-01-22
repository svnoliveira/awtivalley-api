from django.db import models


class Licenca_medica(models.Model):
    ciclo = models.CharField(max_length=127, blank=True)
    data = models.DateField(null=True, blank=True)
    responsavel = models.CharField(max_length=127, blank=True)
    crm = models.CharField(max_length=127, blank=True)
    # user
