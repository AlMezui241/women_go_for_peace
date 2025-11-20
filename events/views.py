# events/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.utils import timezone
from .models import Event

class EventListView(ListView):
    model = Event
    template_name = 'events/list.html'
    context_object_name = 'events'
    
    def get_queryset(self):
        return Event.objects.filter(date__gte=timezone.now()).order_by('date')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['past_events'] = Event.objects.filter(date__lt=timezone.now()).order_by('-date')[:10]
        return context

class EventDetailView(DetailView):
    model = Event
    template_name = 'events/detail.html'
    context_object_name = 'event'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

# events/views.py (ajouts)
from datetime import datetime, timedelta
from django.utils import timezone
from django.views.generic import TemplateView

class CalendarView(TemplateView):
    template_name = 'events/calendar.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Récupérer le mois et l'année demandés
        year = int(self.request.GET.get('year', timezone.now().year))
        month = int(self.request.GET.get('month', timezone.now().month))
        
        # Premier jour du mois
        first_day = timezone.datetime(year, month, 1)
        # Dernier jour du mois
        if month == 12:
            last_day = timezone.datetime(year + 1, 1, 1) - timedelta(days=1)
        else:
            last_day = timezone.datetime(year, month + 1, 1) - timedelta(days=1)
        
        # Événements du mois
        events = Event.objects.filter(
            date__gte=first_day,
            date__lte=last_day
        ).order_by('date')
        
        # Préparer le calendrier
        calendar = self.generate_calendar(year, month, events)
        
        context.update({
            'calendar': calendar,
            'current_month': first_day,
            'prev_month': first_day - timedelta(days=1),
            'next_month': last_day + timedelta(days=1),
            'events': events,
        })
        return context
    
    def generate_calendar(self, year, month, events):
        import calendar
        
        cal = calendar.Calendar(firstweekday=0)  #Lundi en premier
        month_days = cal.monthdayscalendar(year, month)
        
        calendar_data = []
        
        for week in month_days:
            week_data = []
            for day in week:
                if day == 0:
                    week_data.append({'day': None, 'events': []})
                else:
                    day_events = []
                    for event in events:
                        if event.date.day == day and event.date.month == month and event.date.year == year:
                            day_events.append(event)
                    week_data.append({
                        'day': day,
                        'events': day_events,
                        'is_today': (
                            day == timezone.now().day and 
                            month == timezone.now().month and 
                            year == timezone.now().year
                        )
                    })
            calendar_data.append(week_data)
        
        return calendar_data