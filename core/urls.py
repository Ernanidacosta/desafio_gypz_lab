from django.urls import include, path
from.views import SolicitacaoAPIView


urlpatterns = [
    path('solicitacao', SolicitacaoAPIView.as_view(), name='solicitacao'),
]
