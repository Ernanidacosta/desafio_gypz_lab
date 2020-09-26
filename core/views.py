from rest_framework import generics
from rest_framework import viewsets
from .models import Solicitante
from .serializers import SolicitanteSerializer


class SolicitacoesAPIView(generics.ListCreateAPIView):
    queryset = Solicitante.objects.all()
    serializer_class = SolicitanteSerializer

class SolicitacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Solicitante.objects.all()
    serializer_class = SolicitanteSerializer


class SolicitacoesViewSet(viewsets.ModelViewSet):
    queryset = Solicitante.objects.all()
    serializer_class = SolicitanteSerializer
