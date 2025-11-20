# donations/models.py
from django.db import models

class Donation(models.Model):
    AMOUNT_CHOICES = [
        (5000, '5000 Fcfa'),
        (10000, '10000 Fcfa'),
        (15000, '15000 Fcfa'),
        (20000, '20000 Fcfa'),
        (50000, '50000 Fcfa'),
    ]
    
    amount = models.DecimalField(max_digits=10, decimal_places=2, choices=AMOUNT_CHOICES)
    donor_first_name = models.CharField(max_length=100)
    donor_last_name = models.CharField(max_length=100)
    donor_email = models.EmailField()
    donor_phone = models.CharField(max_length=20, blank=True)
    message = models.TextField(blank=True)
    is_anonymous = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Don"
        verbose_name_plural = "Dons"
        ordering = ['-created_at']