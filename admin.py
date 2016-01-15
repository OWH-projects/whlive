from django.contrib import admin 
from models import *

class SegmentAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'show', 'date', 'id' ]
    ordering = [ '-date' ]

class ScheduleAdmin(admin.ModelAdmin):
    list_display = [ 'show', 'date', 'id' ]
    list_filter = [ ]

admin.site.register(Segment, SegmentAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Show)