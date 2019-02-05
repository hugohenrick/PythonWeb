from Cliente.views import IndexTemplateView, ClienteListView, ClienteUpdateView, ClienteCreateView, \
    ClienteDeleteView

from django.urls import path

app_name = 'Cliente'

urlpatterns = [
    # GET /
    path('', IndexTemplateView.as_view(), name="index"),

    # GET /cliente/cadastrar
    path('cliente/cadastrar', ClienteCreateView.as_view(), name="cadastra_cliente"),

    # GET /clientes
    path('clientes/', ClienteListView.as_view(), name="lista_clientes"),

    # GET/POST /cliente/{pk}
    path('cliente/<pk>', ClienteUpdateView.as_view(), name="atualiza_cliente"),

    # GET/POST /clientes/excluir/{pk}
    path('cliente/excluir/<pk>', ClienteDeleteView.as_view(), name="deleta_cliente"),
]
