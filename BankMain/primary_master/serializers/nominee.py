from rest_framework import serializers
from ..models.nominee import Nominee

class NomineeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nominee
        fields = "__all__"