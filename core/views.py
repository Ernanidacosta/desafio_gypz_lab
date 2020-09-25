from rest_framework import generics

from .models import Solicitante
from .serializers import SolicitanteSerializer


class SolicitacaoAPIView(generics.ListCreateAPIView):
    queryset = Solicitante.objects.all()
    serializer_class = SolicitanteSerializer
