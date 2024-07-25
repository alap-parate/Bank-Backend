from rest_framework import viewsets
from ..models.locations import State, District, Taluka
from ..serializers.locations import DistrictSerializer, StateSerializer, TalukaSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']

class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']
    filterset_fields = ['state_id']

class TalukaViewSet(viewsets.ModelViewSet):
    queryset = Taluka.objects.all()
    serializer_class = TalukaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']
    filterset_fields = ['district_id']