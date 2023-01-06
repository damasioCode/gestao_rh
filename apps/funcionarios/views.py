from django.urls import reverse_lazy

from django.contrib.auth.models import User

from django.views.generic import (
    ListView, 
    UpdateView,
    DeleteView,
    CreateView
)

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

class FuncionarioNovo(CreateView):
    model = Funcionario

    fields = [
        'nome',
        'departamentos',
    ]

    def form_valid(self, form):
        req = self.request.user.funcionario

        # Commit não manda ao banco de dados
        funcionario = form.save(commit=False)

        full_name = funcionario.nome.split(' ')
        username = full_name[0] + full_name[1]

        funcionario.empresa = req.empresa
        funcionario.user = User.objects.create(
            username=username
        )

        funcionario.save()

        return super(FuncionarioNovo, self).form_valid(form)