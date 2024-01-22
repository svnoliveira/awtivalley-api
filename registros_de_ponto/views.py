from django.shortcuts import get_object_or_404
from .serializers import RegistroSerializer
from .models import Registro_de_ponto
from users.models import User
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication


class RegistroListCreateView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsSuperUserOrNotSafeMethod]

    serializer_class = RegistroSerializer
    queryset = Registro_de_ponto.objects.all()

    def perform_create(self, serializer):
        user = get_object_or_404(User, pk=self.kwargs["user_id"])
        serializer.save(user=user)


class RegistroRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsSuperUserOrOwnsAccount]

    serializer_class = RegistroSerializer
    queryset = Registro_de_ponto.objects.all()
    lookup_url_kwarg = "ponto_id"
