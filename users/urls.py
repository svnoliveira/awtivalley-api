from django.urls import path
from rest_framework_simplejwt import views
from .views import (
    UserListCreateView,
    UserRetrieveUpdateDestroyView,
    UserUnlinkUpdateView
)


urlpatterns = [
    path("users/", UserListCreateView.as_view()),
    path("users/<int:user_id>/", UserRetrieveUpdateDestroyView.as_view()),
    path(
        "login/", views.TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        "users/cursos/desvincular/<int:user_id>/<int:curso_id>",
        UserUnlinkUpdateView.as_view()
    ),
    path(
        "users/especialidades/desvincular/<int:user_id>/<int:especialidade_id>/",
        UserUnlinkUpdateView.as_view()
    ),
]
