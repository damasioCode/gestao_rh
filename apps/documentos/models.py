from django.db import models
from apps.funcionarios.models import Funcionario

# Create your models here.
class Documento(models.Model):
    descricao = models.CharField(
        verbose_name='Descricao',
        max_length=100
    )

    pertence = models.ForeignKey(
        Funcionario,
        verbose_name='Usuário',
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.descricao