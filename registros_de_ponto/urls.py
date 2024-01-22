from django.urls import path
from .views import (
    RegistroListCreateView,
    RegistroRetrieveUpdateDestroyView,
)


urlpatterns = [
    path("registro-de-ponto/<int:user_id>/", RegistroListCreateView.as_view()),
    path(
        "registro-de-ponto/<int:ponto_id>/",
        RegistroRetrieveUpdateDestroyView.as_view()
    ),
]
