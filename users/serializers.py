from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
from licencas_medicas.models import Licenca_medica
from user_curso.serializers import UserCursoSerializer
from especialidades.serializers import EspecialidadeSerializer
from registros_de_ponto.serializers import RegistroSerializer
from licencas_medicas.serializers import Licenca_medicaSerializer


class UserSerializer(serializers.ModelSerializer):
    cursos = UserCursoSerializer(
        source='usercurso_set',
        many=True,
        read_only=True
    )
    especialidades = EspecialidadeSerializer(many=True, read_only=True)
    registros_de_ponto = RegistroSerializer(many=True, read_only=True)
    licenca_medica = Licenca_medicaSerializer()

    class Meta:
        model = User
        fields = [
            "id",
            "is_superuser",
            "passaporte",
            "senha",
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
            "licenca_medica",
            "registros_de_ponto",
            "ativo",
        ]
        depth = 1
        extra_kwargs = {
            "senha": {'write_only': True, 'source': 'password'},
            "passaporte": {
                "source": "username",
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="A user with that username already exists.",
                    )
                ],
            },
            "is_superuser": {"default": False},
        }

    def create(self, validated_data: dict) -> User:
        licenca_data = validated_data.pop("licenca_medica")
        licenca_medica = Licenca_medica(**licenca_data)
        licenca_medica.save()
        if validated_data["is_superuser"]:
            user = User.objects.create_superuser(
                **validated_data,
                licenca_medica=licenca_medica
            )
        else:
            user = User.objects.create_user(
                **validated_data,
                licenca_medica=licenca_medica
            )
        return user

    def update(self, instance: User, validated_data: dict) -> User:
        licenca_data = validated_data.pop("licenca_medica", None)
        if licenca_data is not None:
            licenca_medica = instance.licenca_medica
            for field, value in licenca_data.items():
                setattr(licenca_medica, field, value)
            licenca_medica.save()
        if validated_data.get("curso"):
            curso = validated_data.pop("curso")
            if curso in instance.cursos.all():
                instance.cursos.remove(curso)
        elif validated_data.get("especialidade"):
            especialidade = validated_data.pop("especialidade")
            if especialidade in instance.especialidades.all():
                instance.especialidades.remove(especialidade)
        else:
            for key, value in validated_data.items():
                if key == "password":
                    instance.set_password(value)
                else:
                    setattr(instance, key, value)
        instance.save()

        return instance
