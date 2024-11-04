from django.shortcuts import get_object_or_404
from .models import Movimentacao
from users.models import User
from produtos.models import Produto
from .serializers import MovimentacaoSerializer
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveDestroyAPIView
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class MovimentacaoListView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = MovimentacaoSerializer
    queryset = Movimentacao.objects.all()


class MovimentacaoCreateView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = MovimentacaoSerializer
    queryset = Movimentacao.objects.all()

    def perform_create(self, serializer):
        user = get_object_or_404(User, pk=self.kwargs["user_id"])
        produto = get_object_or_404(Produto, pk=self.kwargs["produto_id"])
        serializer.save(user=user, produto=produto)


class MovimentacaoRetrieveDestroyView(RetrieveDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = MovimentacaoSerializer
    queryset = Movimentacao.objects.all()
    lookup_url_kwarg = "movimentacao_id"
