from django.shortcuts import render
# donations/views.py
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib import messages
from .models import Donation
from .forms import DonationForm

class DonationView(FormView):
    template_name = 'donations/donate.html'
    form_class = DonationForm
    
    def form_valid(self, form):
        donation = form.save()
        messages.success(self.request, 'Merci pour votre don ! Votre soutien est précieux.')
        return redirect('donations:success', donation_id=donation.id)

def donation_success(request, donation_id):
    donation = Donation.objects.get(id=donation_id)
    return render(request, 'donations/success.html', {'donation': donation})
