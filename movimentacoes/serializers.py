from rest_framework import serializers
from .models import Movimentacao
from produtos.models import Produto


class MovimentacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movimentacao
        fields = [
            "id",
            "user",
            "produto",
            "quantidade",
            "data",
        ]
        extra_kwargs = {
            "user": {'read_only': True},
            "produto": {'read_only': True},
            "data": {'read_only': True},
        }

    def create(self, validated_data: dict) -> Movimentacao:
        produto: Produto = validated_data.get("produto")
        quantidade = validated_data["quantidade"]

        produto.estoque = quantidade
        produto.save()

        return Movimentacao.objects.create(**validated_data)
