from django.urls import path
from .views import (
    CursoListCreateView,
    CursoRetrieveUpdateDestroyView,
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
]
