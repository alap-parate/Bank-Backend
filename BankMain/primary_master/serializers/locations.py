from rest_framework import serializers
from ..models.locations import State, District, Taluka

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = "__all__"

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = "__all__"

class TalukaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taluka
        fields = "__all__"