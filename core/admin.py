from django.contrib import admin

from .models import Solicitante


@admin.register(Solicitante)
class SolicitanteAdmin(admin.ModelAdmin):
    list_display = ('ativo', 'nome', 'renda', 'limit', 'score', 'criacao', 'atualizacao')
