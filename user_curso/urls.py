from django.urls import path

from .views import UserCursoUpdateView


urlpatterns = [
    path(
        "cursos/vincular/<int:curso_id>/<int:user_id>/",
        UserCursoUpdateView.as_view()
    ),
]
