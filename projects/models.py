# projects/models.py
from django.db import models
from django.utils import timezone

class Project(models.Model):
    STATUS_CHOICES = [
        ('ongoing', 'En cours'),
        ('completed', 'Terminé'),
        ('planned', 'Planifié'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    short_description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='projects/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ongoing')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Projet"
        verbose_name_plural = "Projets"
        ordering = ['-created_at']
