from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Solicitante
from .serializers import SolicitanteSerializer, Solicitante


class SolicitacaoAPIView(APIView):

    def get(self, request):
        solicitacoes = Solicitante.objects.all()
        serializer = SolicitanteSerializer(solicitacoes, many=True)
        return Response(serializer.data)

    def post(self, requests):
        serializer = SolicitanteSerializer(data=requests.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(serializer.data, status=status.HTTP_201_CREATED)
