from django.shortcuts import get_object_or_404
from .serializers import RegistroSerializer
from django.db.models.query import QuerySet
from .models import Registro_de_ponto
from users.models import User
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication


class RegistroListView(ListAPIView):
    authentication_classes = [JWTAuthentication]

    serializer_class = RegistroSerializer
    queryset = Registro_de_ponto.objects.all()


class RegistroListCreateView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsSuperUserOrNotSafeMethod]

    serializer_class = RegistroSerializer
    queryset = Registro_de_ponto.objects.all()
    lookup_url_kwarg = "user_id"

    def get_queryset(self):
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
            % self.__class__.__name__
        )

        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = queryset.filter(user=self.kwargs["user_id"])
        return queryset

    def perform_create(self, serializer):
        user = get_object_or_404(User, pk=self.kwargs["user_id"])
        serializer.save(user=user)


class RegistroRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsSuperUserOrOwnsAccount]

    serializer_class = RegistroSerializer
    queryset = Registro_de_ponto.objects.all()
    lookup_url_kwarg = "ponto_id"
