# core/models.py
from django.db import models
from django.contrib.auth.models import User

class Organization(models.Model):
    name = models.CharField(max_length=200)
    mission = models.TextField()
    vision = models.TextField()
    history = models.TextField()
    values = models.TextField()
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)
    address = models.TextField()
    
    class Meta:
        verbose_name = "Organisation"
        verbose_name_plural = "Organisations"

class SocialMedia(models.Model):
    PLATFORM_CHOICES = [
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter'),
        ('instagram', 'Instagram'),
        ('linkedin', 'LinkedIn'),
        ('youtube', 'YouTube'),
    ]
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    url = models.URLField()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Réseau social"
        verbose_name_plural = "Réseaux sociaux"
