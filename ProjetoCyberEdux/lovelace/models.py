from django.db import models
from django.contrib.auth.models import User


class Aluno(models.Model):
    data_nascimento = models.DateField(null=True, default=None)
    data_matricula = models.DateField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)