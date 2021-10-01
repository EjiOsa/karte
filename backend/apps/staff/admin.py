from django.contrib import admin
from .models import Staff, Job, Role

# Register your models here.

@admin.register(Staff)
class Staff(admin.ModelAdmin):
    pass

@admin.register(Job)
class Job(admin.ModelAdmin):
    pass

@admin.register(Role)
class Role(admin.ModelAdmin):
    pass