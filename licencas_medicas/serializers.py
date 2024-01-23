from rest_framework import serializers
from .models import Licenca_medica


class Licenca_medicaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Licenca_medica
        fields = [
            "ciclo",
            "data",
            "responsavel",
            "crm"
        ]
