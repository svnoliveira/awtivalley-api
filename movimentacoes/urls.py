from django.urls import path
from .views import (
     MovimentacaoListView,
     MovimentacaoCreateView,
     MovimentacaoRetrieveDestroyView
)


urlpatterns = [
    path(
        "movimentacoes/", MovimentacaoListView.as_view()
    ),
    path(
        "movimentacoes/<user_id>/<produto_id>/",
        MovimentacaoCreateView.as_view()
    ),
    path(
        "movimentacoes/<int:movimentacao_id>/",
        MovimentacaoRetrieveDestroyView.as_view()
    ),
]
