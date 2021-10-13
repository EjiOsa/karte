from rest_framework import serializers
from .models import *
# from django.db.models import fields

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('last_name','first_name','last_name_kana','first_name_kana','age','sex','level','disease',)