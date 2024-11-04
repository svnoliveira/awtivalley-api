from rest_framework import serializers
from .models import Produto
from rest_framework.validators import UniqueValidator


class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        fields = [
            "id",
            "imagem",
            "nome",
            "categoria",
            "preco",
            "estoque",
            "qtdCondicao",
            "movimentacoes"
        ]
        extra_kwargs = {
            "movimentacoes": {'read_only': True, 'many': True},
            "nome": {
                "validators": [
                    UniqueValidator(
                        queryset=Produto.objects.all(),
                        message="Produto already exists.",
                    )
                ],
            }
        }
