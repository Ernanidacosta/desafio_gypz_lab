from core.serializers import SolicitanteSerializer
from django.shortcuts import render
from rest_framework import viewsets
from .models import Solicitante

class SolicitanteViewSet(viewsets.ModelViewSet):
    queryset = Solicitante.objects.all()
    serializer_class = SolicitanteSerializer