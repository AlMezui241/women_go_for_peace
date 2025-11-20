# events/urls.py (mise à jour)
from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.EventListView.as_view(), name='list'),
    path('calendrier/', views.CalendarView.as_view(), name='calendar'),
    path('<int:pk>/', views.EventDetailView.as_view(), name='detail'),
]