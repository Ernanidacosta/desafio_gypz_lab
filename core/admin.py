from django.contrib import admin
from .models import Solicitante

class SolicitanteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'status']

admin.site.register(Solicitante, SolicitanteAdmin)