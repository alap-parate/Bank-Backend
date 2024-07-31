from rest_framework import serializers
from ..models.locations import State, District, Taluka, City, Zone

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
        
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"
        
class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = "__all__"