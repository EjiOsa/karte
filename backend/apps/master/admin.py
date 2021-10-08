from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Disease)
class Disease(admin.ModelAdmin):
    pass

@admin.register(Rest)
class Rest(admin.ModelAdmin):
    pass

@admin.register(Role)
class Role(admin.ModelAdmin):
    pass