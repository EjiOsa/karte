from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Doctor)
class Doctor(admin.ModelAdmin):
    pass

@admin.register(Nurse)
class Nurse(admin.ModelAdmin):
    pass

@admin.register(Pharmacist)
class Pharmacist(admin.ModelAdmin):
    pass

@admin.register(Physical)
class Physical(admin.ModelAdmin):
    pass

@admin.register(Occupational)
class Occupational(admin.ModelAdmin):
    pass

@admin.register(Clerk)
class Clerk(admin.ModelAdmin):
    pass
