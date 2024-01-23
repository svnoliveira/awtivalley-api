from django.urls import path
from .views import (
    CursoListCreateView,
    CursoRetrieveUpdateDestroyView,
    CursoRegisterUpdateView,
)


urlpatterns = [
    path(
        "cursos/",
        CursoListCreateView.as_view()
    ),
    path(
        "cursos/<int:curso_id>/",
        CursoRetrieveUpdateDestroyView.as_view()
    ),
    path(
        "cursos/vincular/<int:curso_id>/<int:user_id>/",
        CursoRegisterUpdateView.as_view()
    ),
]
