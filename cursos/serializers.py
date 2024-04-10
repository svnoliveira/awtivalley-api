from rest_framework import serializers
from .models import Curso
from user_curso.models import UserCurso
from datetime import datetime, timedelta
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

    def update(
            self, instance: Curso, validated_data: dict
            ) -> Curso:
        if validated_data.get("user"):
            user = validated_data.pop("user")
            if instance.validade > 0:
                validade = instance.validade
                inicio = datetime.now()
                vencimento = inicio + timedelta(days=validade)
                if not UserCurso.objects.filter(
                    user=user,
                    curso=instance
                ).exists():
                    UserCurso.objects.create(
                        user=user,
                        curso=instance,
                        inicio=inicio,
                        vencimento=vencimento
                    )
                else:
                    ...
            else:
                if not instance.users.filter(id=user.id).exists():
                    instance.users.add(user)
                    instance.save()
                return instance
        else:
            for key, value in validated_data.items():
                setattr(instance, key, value)
        instance.save()
        return instance
