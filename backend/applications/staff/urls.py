# from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('docter', DocterViewSet)
router.register('nurse', NurseViewSet)
router.register('pharmacist', PharmacistViewSet)
router.register('physical', PhysicalViewSet)
router.register('occupational', OccupationalViewSet)
router.register('clerk', ClerkViewSet)
