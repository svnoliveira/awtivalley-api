from django.urls import path
from .views import (
    RegistroListView,
    RegistroListCreateView,
    RegistroRetrieveUpdateDestroyView,
)


urlpatterns = [
    path("registro-de-ponto/", RegistroListView.as_view()),
    path(
        "registro-de-ponto/user/<int:user_id>/",
        RegistroListCreateView.as_view()
    ),
    path(
        "registro-de-ponto/<int:ponto_id>/",
        RegistroRetrieveUpdateDestroyView.as_view()
    ),
]
