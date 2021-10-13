import django_filters
from rest_framework import viewsets, filters

from .models import Patient
from .serializer import PatientSerializer
# from django.shortcuts import render

# Create your views here.

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer