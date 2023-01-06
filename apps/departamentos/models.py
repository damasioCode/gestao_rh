from django.db import models
from apps.empresas.models import Empresa

# Create your models here.
class Departamento(models.Model):
    nome = models.CharField(
        verbose_name='Nome',
        max_length=70
    )

    empresa = models.ForeignKey(
        Empresa,
        verbose_name='Empresa',
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.nome