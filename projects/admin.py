# projects/admin.py
from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'start_date', 'created_at']
    list_filter = ['status', 'start_date']
    search_fields = ['title', 'description']
    date_hierarchy = 'created_at'
