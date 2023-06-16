from django.contrib import admin
from .models import Ride

# Register your models here.
# admin.site.register(Rallies)


@admin.register(Ride)
class RidesAdmin(admin.ModelAdmin):
    # list_display = ('name', 'start_date', 'distance', 'total_time')
    list_display = ('name', 'start_date', 'total_time')
    list_filter = ('name',)
    # ordering = ('distance', 'total_time')
    ordering = ('total_time',)
    search_fields = ('name',)
    date_hierarchy = 'start_date'