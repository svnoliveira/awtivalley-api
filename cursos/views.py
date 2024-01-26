from django.shortcuts import get_object_or_404
from .serializers import CursoSerializer
from .models import Curso
from users.models import User
from rest_framework.generics import (
    ListCreateAPIView,
    UpdateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class CursoListCreateView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = CursoSerializer
    queryset = Curso.objects.all()


class CursoRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = CursoSerializer
    queryset = Curso.objects.all()
    lookup_url_kwarg = "curso_id"


class CursoRegisterUpdateView(UpdateAPIView):
    authentication_classes = [JWTAuthentication]

    serializer_class = CursoSerializer
    queryset = Curso.objects.all()
    lookup_url_kwarg = "curso_id"

    def perform_update(self, serializer):
        user = get_object_or_404(User, pk=self.kwargs["user_id"])
        serializer.save(user=user)
