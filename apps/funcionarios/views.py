from django.views.generic import (
    ListView, 
    UpdateView,
    DeleteView
)

from django.urls import reverse_lazy

from .models import Funcionario

# Create your views here.

class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa

        queryset = Funcionario.objects.filter(
            empresa=empresa_logada
        )

        return queryset

class FuncionarioEdit(UpdateView):
    model = Funcionario

    fields = [
        'nome',
        'departamentos',
    ]

class FuncionarioDelete(DeleteView):
    model = Funcionario

    success_url = reverse_lazy('list_funcionarios')
