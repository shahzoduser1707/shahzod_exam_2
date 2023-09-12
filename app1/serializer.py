from rest_framework import serializers
from .models import Ustalar,Orderlar


class UstalarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ustalar
        fields = ('__all__')


class OrderlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orderlar
        fields = ('__all__')