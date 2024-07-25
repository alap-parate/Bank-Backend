from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.locations import DistrictViewSet, StateViewSet, TalukaViewSet

router = DefaultRouter()
router.register(r'states', StateViewSet)
router.register(r'districts', DistrictViewSet)
router.register(r'talukas',TalukaViewSet)

urlpatterns = [
    path('',include(router.urls))
]
