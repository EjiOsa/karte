from django_filters import rest_framework as filters
from rest_framework import viewsets

from .models import *
from .serializer import *
# from django.shortcuts import render

class DoctorFilter(filters.FilterSet):
    # フィルタの定義(カラム名と同名なら、field_nameは不要)
    created = filters.DateFilter(field_name = 'created_at', lookup_expr = 'gte')
    class Meta:
        model = Doctor
        fields = ['sex', 'role', 'created']
# Create your views here.
class DocterViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_class = DoctorFilter

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