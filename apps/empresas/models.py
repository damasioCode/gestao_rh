from django.db import models
from django.urls import reverse

# Create your models here.
class Empresa(models.Model):
    nome = models.CharField(
        max_length=100,
        verbose_name='Nome da Empresa'
    )

    def get_absolute_url(self):
        return reverse("home")
    

    def __str__(self):
        return self.nome
