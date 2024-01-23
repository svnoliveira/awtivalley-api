from django.urls import path
from .views import (
    EspecialidadeListCreateView,
    EspecialidadeRetrieveUpdateDestroyView,
    EspecialidadeRegisterUpdateView,
)


urlpatterns = [
    path(
        "especialidades/",
        EspecialidadeListCreateView.as_view()
    ),
    path(
        "especialidades/<int:especialidade_id>/",
        EspecialidadeRetrieveUpdateDestroyView.as_view()
    ),
    path(
        "especialidades/vincular/<int:especialidade_id>/<int:user_id>/",
        EspecialidadeRegisterUpdateView.as_view()
    ),
]
