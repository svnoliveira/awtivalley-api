from rest_framework import serializers
from .models import Curso
from rest_framework.validators import UniqueValidator


class CursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = [
            "id",
            "nome",
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

    def update(
            self, instance: Curso, validated_data: dict
            ) -> Curso:
        if validated_data.get("user"):
            user = validated_data.pop("user")
            instance.users.add(user)
        else:
            for key, value in validated_data.items():
                setattr(instance, key, value)
        instance.save()
        return instance
