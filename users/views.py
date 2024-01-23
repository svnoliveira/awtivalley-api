from django.shortcuts import get_object_or_404

from _core.permissions import IsSuperUserOrOwnsAccount
from .serializers import UserSerializer
from .models import User
from cursos.models import Curso
from especialidades.models import Especialidade
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    UpdateAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication


class UserListCreateView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUserOrOwnsAccount]

    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_url_kwarg = "user_id"


class UserUnlinkUpdateView(UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUserOrOwnsAccount]

    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_url_kwarg = "user_id"

    def perform_update(self, serializer):
        if self.kwargs.get("curso_id"):
            curso = get_object_or_404(Curso, pk=self.kwargs["curso_id"])
        else:
            curso = False
        if self.kwargs.get("especialidade_id"):
            especialidade = get_object_or_404(
                Especialidade, pk=self.kwargs["especialidade_id"]
            )
        else:
            especialidade = False
        serializer.save(curso=curso, especialidade=especialidade)
