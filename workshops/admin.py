from django.contrib import admin
from .models import Workshops

# Register your models here.

class WorkshopsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'duration',
        'date',
        'time',
        'location',
        'image',
    )

admin.site.register(Workshops, WorkshopsAdmin)