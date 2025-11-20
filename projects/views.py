
# projects/views.py
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Project

class ProjectListView(ListView):
    model = Project
    template_name = 'projects/list.html'
    context_object_name = 'projects'
    paginate_by = 9
    
    def get_queryset(self):
        return Project.objects.all().order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ongoing_projects'] = Project.objects.filter(status='ongoing')
        context['completed_projects'] = Project.objects.filter(status='completed')
        return context

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/detail.html'
    context_object_name = 'project'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Projets similaires
        context['related_projects'] = Project.objects.filter(
            status=self.object.status
        ).exclude(id=self.object.id)[:3]
        return context