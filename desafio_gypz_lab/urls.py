from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from core.views import SolicitanteViewSet
from core.urls import solicitacao_rota

router = routers.DefaultRouter()
router.register(r'solicitantes', SolicitanteViewSet)


urlpatterns = [
    path('api/', include(solicitacao_rota.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('django.contrib.auth.urls')),
]
