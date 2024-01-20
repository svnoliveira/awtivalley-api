from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # is_superuser
    # username => passaporte
    # password => senha
    nome = models.CharField(max_length=127)
    discord_id = models.CharField(max_length=50, unique=True)
    cargo = models.CharField(max_length=127)
    efetivacao = models.DateField()
    funcao = models.CharField(max_length=127)
    setor = models.CharField(max_length=127)
    ultima_promocao = models.DateField()
    observacoes = models.TextField()
    funcoes_extra = models.TextField()
    especialidades = models.ManyToManyField(
        "especialidades.Especialidade", related_name="users"
    )
    cursos = models.ManyToManyField(
        "cursos.Curso", related_name="users"
    )
    licenca_medica = models.OneToOneField(
        "licencas_medicas.Licenca_medica", on_delete=models.CASCADE
    )
    # registros_de_ponto 1TM
