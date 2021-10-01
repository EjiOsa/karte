from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Disease, Patient,Rest

# Register your models here.

@admin.register(Disease)
class Disease(admin.ModelAdmin):
    pass

@admin.register(Rest)
class Rest(admin.ModelAdmin):
    pass

@admin.register(Patient)
class Patient(admin.ModelAdmin):
    pass