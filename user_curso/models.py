from django.db import models
from cursos.models import Curso
from users.models import User


class UserCurso(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    inicio = models.DateField(null=True)
    vencimento = models.DateField(null=True)
