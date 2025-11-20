
# core/views.py
from django.shortcuts import render, redirect
from blog.models import Post
from projects.models import Project
from events.models import Event
# core/views.py (ajout)
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm


def home(request):
    featured_projects = Project.objects.filter(status='ongoing')[:3]
    recent_posts = Post.objects.filter(published=True)[:3]
    upcoming_events = Event.objects.all()[:2]
    
    context = {
        'featured_projects': featured_projects,
        'recent_posts': recent_posts,
        'upcoming_events': upcoming_events,
    }
    return render(request, 'core/home.html', context)

def about(request):
    return render(request, 'core/about.html')



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Envoyer l'email (à configurer avec les paramètres SMTP)
            send_mail(
                subject=f"Contact Women Go for Peace: {form.cleaned_data['subject']}",
                message=f"De: {form.cleaned_data['name']} ({form.cleaned_data['email']})\n\n{form.cleaned_data['message']}",
                from_email='noreply@womengoforpeace.org',
                recipient_list=['contact@womengoforpeace.org'],
            )
            messages.success(request, 'Votre message a été envoyé avec succès ! Nous vous répondrons dans les plus brefs délais.')
            return redirect('core:contact')
    else:
        form = ContactForm()
    
    return render(request, 'core/contact.html', {'form': form})