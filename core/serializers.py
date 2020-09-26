from rest_framework import serializers
import random

from .models import Solicitante


def aprova(validacao):
    nota = random.randint(1, 999)
    solicitacao = Solicitante.objects.create(**validacao)
    solicitacao.pontos = nota
    solicitacao.status = True

    if nota < 300:
        solicitacao.status = False

    elif 300 <= nota < 600:
        solicitacao.limite = 1000

    elif 600 <= nota < 800:
        solicitacao.limite = validacao['renda'] * 0.5
        if solicitacao.limite < 1000:
            solicitacao.limite = 1000

    elif 800 <= nota <= 950:
        solicitacao.limite = validacao['renda'] * 2

    elif nota >= 951:
        solicitacao.limite = 1000000

    try:
        solicitacao.save()
        return solicitacao
    except:
        return {'message': 'Ocorreu um Erro na Solicitação'}


class SolicitanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitante
        fields = ('id', 'nome', 'renda', 'score')
