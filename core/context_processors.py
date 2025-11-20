# core/context_processors.py
from .models import Organization, SocialMedia

def organization_info(request):
    try:
        organization = Organization.objects.first()
        social_media = SocialMedia.objects.all()
    except:
        organization = None
        social_media = []
    
    return {
        'organization': organization,
        'social_media': social_media,
    }