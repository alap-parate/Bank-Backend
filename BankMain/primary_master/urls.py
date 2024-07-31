from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.locations import DistrictViewSet, StateViewSet, TalukaViewSet, CityViewSet, ZoneViewSet
from .views.nominee import NomineeViewSet

router = DefaultRouter()
router.register(r'state', StateViewSet)
router.register(r'district', DistrictViewSet)
router.register(r'taluka',TalukaViewSet)
router.register(r'city',CityViewSet)
router.register(r'zone',ZoneViewSet)
router.register(r'nominee',NomineeViewSet)

urlpatterns = [
    path('',include(router.urls))
]
