from django.db import models
from django.contrib.auth.models import User


class Projeto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    cliente = models.CharField(max_length=200)
    data_inicio = models.DateField()
    data_prevista_conclusao = models.DateField()
    data_real_conclusao = models.DateField(blank=True, null=True)
    responsavel = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Status(models.TextChoices):
    PENDENTE = 'Pendente', 'Pendente'
    EM_ANDAMENTO = 'Em andamento', 'Em andamento'
    ATRASADO = 'Atrasado', 'Atrasado'
    BLOQUEADO = 'Bloqueado', 'Bloqueado'
    CONCLUIDO = 'Concluído', 'Concluído'


class Atividade(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='atividades')
    descricao = models.CharField(max_length=300)
    responsavel = models.ForeignKey(User, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_prevista_conclusao = models.DateField()
    data_real_conclusao = models.DateField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDENTE
    )
    motivo_status = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.descricao} ({self.projeto.nome})"

