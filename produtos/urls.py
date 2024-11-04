from django.urls import path
from .views import (
     ProdutoListCreateView,
     ProdutoRetrieveUpdateDestroyView
)


urlpatterns = [
    path(
        "produtos/",
        ProdutoListCreateView.as_view()
    ),
    path(
        "produtos/<int:produto_id>/",
        ProdutoRetrieveUpdateDestroyView.as_view()
    ),
]
