# events/admin.py
from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'location', 'created_at']
    list_filter = ['date', 'created_at']
    search_fields = ['title', 'description', 'location']
    date_hierarchy = 'date'
    fieldsets = (
        ('Informations générales', {
            'fields': ('title', 'description', 'image')
        }),
        ('Détails pratiques', {
            'fields': ('date', 'location', 'registration_link')
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).order_by('-date')
