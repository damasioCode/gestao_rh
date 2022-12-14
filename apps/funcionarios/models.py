from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa

# Create your models here.
class Funcionario(models.Model):
    nome = models.CharField(
        verbose_name="Nome",
        max_length=100,
    )
    
    user = models.OneToOneField(
        User,
        verbose_name='Usuário',
        on_delete=models.PROTECT
    )

    departamentos = models.ManyToManyField(
        Departamento,
        verbose_name='Departamentos'
    )

    empresa = models.ForeignKey(
        Empresa,
        verbose_name='Empresa',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    def get_absolute_url(self):
        return reverse("list_funcionarios")
    
    def __str__(self):
        return self.nome