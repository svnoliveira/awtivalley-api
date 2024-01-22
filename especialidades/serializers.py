from rest_framework import serializers
from .models import Especialidade


class EspecialidadeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Especialidade
        fields = [
            "id",
            "nome",
            "users",
        ]
        extra_kwargs = {
            "users": {'read_only': True, 'many': True},
        }

    def update(
            self, instance: Especialidade, validated_data: dict
            ) -> Especialidade:
        if validated_data["user"]:
            user = validated_data.pop("user")
            instance.users.add(user)
        else:
            for key, value in validated_data.items():
                setattr(instance, key, value)
        instance.save()
        return instance
