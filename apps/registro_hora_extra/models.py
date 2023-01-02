from django.db import models
from apps.funcionarios.models import Funcionario

# Create your models here.
class RegistroHoraExtra(models.Model):
    motivo = models.CharField(
        verbose_name='Motivo',
        max_length=100
    )

    funcionario = models.ForeignKey(
        Funcionario,
        verbose_name='Funcionario',
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.motivo