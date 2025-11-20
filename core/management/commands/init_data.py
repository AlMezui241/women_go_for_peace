# core/management/commands/init_data.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Organization, SocialMedia
from django.utils.text import slugify
from blog.models import Category

class Command(BaseCommand):
    help = 'Initialize basic data for the application'
    
    def handle(self, *args, **options):
        # Créer l'organisation
        organization, created = Organization.objects.get_or_create(
            name="Women Go for Peace",
            defaults={
                'mission': "Œuvrer pour la paix et les droits des femmes à travers le monde...",
                'vision': "Un monde où les femmes sont pleinement actrices des processus de paix...",
                'history': "Fondée en 2010, Women Go for Peace est née de la conviction que...",
                'values': "Égalité, Justice, Solidarité, Paix",
                'contact_email': "contact@womengoforpeace.org",
                'contact_phone': "+241 077 44 41 34",
                'address': "Libreville, Gabon"
            }
        )
        
        # Créer des catégories de blog
        categories = [
            'Actualités',
            'Témoignages',
            'Réflexions',
            'Actions sur le terrain'
        ]
        
        for cat_name in categories:
            slug = slugify(cat_name)
            Category.objects.get_or_create(name=cat_name, defaults={'slug': slug})
        
        self.stdout.write(
            self.style.SUCCESS('Données initiales créées avec succès!')
        )