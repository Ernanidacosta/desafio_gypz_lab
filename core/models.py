from django.db import models
from django.forms import CharField


class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Solicitante(Base):
    nome: CharField = models.CharField(max_length=50, verbose_name='nome')
    score = models.IntegerField(default=0)
    renda = models.FloatField()
    limit = models.FloatField('Limite', default=0)

    def __str__(self) -> str:
        return f'{self.nome}, Limite de: {self.limit}'
