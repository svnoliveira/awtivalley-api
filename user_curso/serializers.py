from rest_framework import serializers
from .models import UserCurso


class UserCursoSerializer(serializers.ModelSerializer):
    nome = serializers.SerializerMethodField()

    class Meta:

        model = UserCurso
        fields = [
            "inicio",
            "vencimento",
            "nome"
        ]

    def get_nome(self, obj):
        return obj.curso.nome
