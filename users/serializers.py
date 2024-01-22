from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    # comments = CommentSerializer(
    #     source='comment_set',
    #     many=True,
    #     read_only=True
    # )
    # orders = OrderSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "is_superuser",
            "passaporte",
            "senha"
            "nome",
            "discord_id",
            "cargo",
            "efetivacao",
            "funcao",
            "setor",
            "ultima_promocao",
            "observacoes",
            "funcoes_extra",
            "especialidades",
            "cursos",
            "licensa_medica",
            "registros_de_ponto",
        ]
        depth = 1
        extra_kwargs = {
            "senha": {'write_only': True, 'source': 'password'},
            "passaporte": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="A user with that username already exists.",
                    )
                ],
                "source": "username",
            },
            "is_superuser": {"default": False},
        }

    def create(self, validated_data: dict) -> User:
        if validated_data["is_superuser"]:
            user = User.objects.create_superuser(**validated_data)
        else:
            user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance: User, validated_data: dict) -> User:
        if validated_data["curso"]:
            curso = validated_data.pop("curso")
            instance.cursos.remove(curso)
        elif validated_data["especialidade"]:
            especialidade = validated_data.pop("especialidade")
            instance.especialidades.remove(especialidade)
        else:
            for key, value in validated_data.items():
                if key == "password":
                    instance.set_password(value)
                else:
                    setattr(instance, key, value)
        instance.save()

        return instance
