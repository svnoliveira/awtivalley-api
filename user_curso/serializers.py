from rest_framework import serializers
from .models import UserCurso
from datetime import datetime, timedelta


class UserCursoSerializer(serializers.ModelSerializer):
    nome = serializers.SerializerMethodField()

    class Meta:

        model = UserCurso
        fields = [
            "nome",
            "inicio",
            "vencimento",
            "certificado"
        ]

    def get_nome(self, obj):
        return obj.curso.nome

    def update(self, instance: UserCurso, validated_data: dict) -> UserCurso:
        if instance.curso.validade > 0:
            validade = instance.curso.validade
            inicio = datetime.now()
            vencimento = inicio + timedelta(days=validade)
            setattr(instance, 'inicio', inicio.date())
            setattr(instance, 'vencimento', vencimento.date())

        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
