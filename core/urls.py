from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import (SolicitacaoAPIView,
                    SolicitacoesAPIView,
                    SolicitacaoAPIView,
                    SolicitacoesViewSet
                    )

router = SimpleRouter()
router.register('solicitacoes', SolicitacoesViewSet)



urlpatterns = [
    path('solicitacoes/', SolicitacoesAPIView.as_view(), name='solicitacoes'),
    path('solicitacao/<int:pk>/', SolicitacaoAPIView.as_view(), name='solicitacao'),
]
