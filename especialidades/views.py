from django.shortcuts import get_object_or_404
from .serializers import EspecialidadeSerializer
from .models import Especialidade
from users.models import User
from rest_framework.generics import (
    ListCreateAPIView,
    UpdateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class EspecialidadeListCreateView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = EspecialidadeSerializer
    queryset = Especialidade.objects.all()


class EspecialidadeRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = EspecialidadeSerializer
    queryset = Especialidade.objects.all()
    lookup_url_kwarg = "especialidade_id"


class EspecialidadeRegisterUpdateView(UpdateAPIView):
    authentication_classes = [JWTAuthentication]

    serializer_class = EspecialidadeSerializer
    queryset = Especialidade.objects.all()
    lookup_url_kwarg = "especialidade_id"

    def perform_update(self, serializer):
        user = get_object_or_404(User, pk=self.kwargs["user_id"])
        serializer.save(user=user)
