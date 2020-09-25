from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Solicitante
from core.serializers import SolicitanteSerializer
from rest_framework.viewsets import ModelViewSet


class SolicitacaoViewset(ModelViewSet):
    serializer_class = SolicitanteSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return Solicitante.objects.all()

    def list(self, request, *args, **kwargs):
        return super(SolicitacaoViewset, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(SolicitacaoViewset, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(SolicitacaoViewset, self).destroy(request, *args, **kwargs)
