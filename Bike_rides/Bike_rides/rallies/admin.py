from django.contrib import admin
from .models import Rally, ParticipantsList

@admin.register(Rally)
class RalliesAdmin(admin.ModelAdmin):
    list_display = ('description', 'date', 'place', 'level')
    list_filter = ('level', 'place')
    search_fields = ('description', 'place', 'level')
    ordering = ('level', 'date')
    date_hierarchy = 'date'
    list_per_page = 10

@admin.register(ParticipantsList)
class PartcipantsListAdmin(admin.ModelAdmin):
    list_display = ('id_participant', 'id_rally')
    list_filter = ('id_participant', 'id_rally')
    ordering = ('id_participant', 'id_rally')


# @admin.register(Ride)
# class RidesAdmin(admin.ModelAdmin):
#     # list_display = ('name', 'start_date', 'distance', 'total_time')
#     list_display = ('name', 'start_date', 'total_time')
#     list_filter = ('name',)
#     # ordering = ('distance', 'total_time')
#     ordering = ('total_time',)
#     search_fields = ('name',)
#     date_hierarchy = 'start_date'


