from rest_framework import serializers
from .models import Curso


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
        }

    def update(
            self, instance: Curso, validated_data: dict
            ) -> Curso:
        if validated_data["user"]:
            user = validated_data.pop("user")
            instance.users.add(user)
        else:
            for key, value in validated_data.items():
                setattr(instance, key, value)
        instance.save()
        return instance
