from django.db.models.expressions import Random
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Solicitante
import random


class SolicitanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitante
        fields = ('id', 'nome', 'renda', 'score')

    def aprova(self, validacao):

        nota = random.randint(1, 199)
        solicitacao = Solicitante.objects.create(**validacao)
        solicitacao.pontos = nota
        solicitacao.status = True

        if nota < 300:
            solicitacao.status = False

        elif nota >= 300 and nota < 600:
            solicitacao.limite = 1000
        
        elif nota >= 600 and nota < 800:
            solicitacao.limite = validacao['renda'] * 1.5
            if solicitacao.limite < 1000:
                solicitacao.limite = 1000
        
        elif nota >= 800 and nota <= 950:
            solicitacao.limite = validacao['renda'] * 2

        elif nota >= 951:
            solicitacao.limite = 1000000

        try:
            solicitacao.save
            return solicitacao
        except:
            return {'message': 'Ocorreu um erro na solicitação'}