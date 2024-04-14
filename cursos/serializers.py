from rest_framework import serializers
from .models import Curso
from rest_framework.validators import UniqueValidator


class CursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = [
            "id",
            "nome",
            "validade",
            "users",
        ]
        extra_kwargs = {
            "users": {'read_only': True, 'many': True},
            "nome": {
                "validators": [
                    UniqueValidator(
                        queryset=Curso.objects.all(),
                        message="Curso already exists.",
                    )
                ],
            }
        }
