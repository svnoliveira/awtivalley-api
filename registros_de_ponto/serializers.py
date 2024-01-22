from rest_framework import serializers
from .models import Registro_de_ponto
import datetime as dt


class RegistroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Registro_de_ponto
        fields = [
            "id",
            "entrada",
            "saida",
            "horas"
            "justificativa",
            "user",
        ]
        depth = 1
        extra_kwargs = {
            "user": {'read_only': True},
            "horas": {'read_only': True},
        }

    def create(self, validated_data: dict) -> Registro_de_ponto:
        horas = {}
        data_dict = {}
        for key, value in validated_data.items():
            if key == "entrada":
                horas["entrada"] = dt.datetime(value)
                data_dict[key] = dt.datetime(value)
            elif key == "saida":
                horas["saida"] = dt.datetime(value)
                data_dict[key] = dt.datetime(value)
            else:
                data_dict[key] = value

        seconds = (horas["saida"] - horas["entrada"]).total_seconds()
        hours = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        time = dt.time(hours, minutes, seconds)
        data_dict["horas"] = time

        instance = Registro_de_ponto.objects.create(**data_dict)
        return instance

    def update(
            self, instance: Registro_de_ponto, validated_data: dict
            ) -> Registro_de_ponto:
        horas = {}
        for key, value in validated_data.items():
            if key == "entrada":
                horas["entrada"] = dt.datetime(value)
                setattr(instance, key, dt.datetime(value))
            elif key == "saida":
                horas["saida"] = dt.datetime(value)
                setattr(instance, key, dt.datetime(value))
            else:
                setattr(instance, key, value)
        seconds = (horas["saida"] - horas["entrada"]).total_seconds()
        hours = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        time = dt.time(hours, minutes, seconds)
        setattr(instance, "horas", time)
        instance.save()

        return instance
