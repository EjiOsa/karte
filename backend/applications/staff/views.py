import django_filters
from rest_framework import viewsets, filters

from .models import *
from .serializer import *
# from django.shortcuts import render

# Create your views here.
class DocterViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_fields = ('sex','role')

class NurseViewSet(viewsets.ModelViewSet):
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer

class PharmacistViewSet(viewsets.ModelViewSet):
    queryset = Pharmacist.objects.all()
    serializer_class = PharmacistSerializer

class PhysicalViewSet(viewsets.ModelViewSet):
    queryset = Physical.objects.all()
    serializer_class = PhysicalSerializer

class OccupationalViewSet(viewsets.ModelViewSet):
    queryset = Occupational.objects.all()
    serializer_class = OccupationalSerializer

class ClerkViewSet(viewsets.ModelViewSet):
    queryset = Clerk.objects.all()
    serializer_class = ClerkSerializer