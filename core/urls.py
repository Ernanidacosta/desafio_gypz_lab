from rest_framework.routers import DefaultRouter
from core.viewsets import SolicitacaoViewset

solicitacao_rota = DefaultRouter()
solicitacao_rota.register('solicitacao', SolicitacaoViewset, basename='Solicitacao')