from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Patient

# Register your models here.

@admin.register(Patient)
class Patient(admin.ModelAdmin):
    pass