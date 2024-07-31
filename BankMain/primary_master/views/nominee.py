from rest_framework import viewsets
from ..models.nominee import Nominee
from ..serializers.nominee import NomineeSerializer 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class NomineeViewSet(viewsets.ModelViewSet):
    queryset = Nominee.objects.all()
    serializer_class = NomineeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']