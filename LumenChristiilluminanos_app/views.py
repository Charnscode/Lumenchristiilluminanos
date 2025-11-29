from django.shortcuts import render
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.html import strip_tags
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.
def home(request):
    return render(request, 'LumenChristiilluminanos_app/index.html')

def about(request):
    return render(request, 'LumenChristiilluminanos_app/about.html')

def prions(request):
    return render(request, 'LumenChristiilluminanos_app/prions.html')

def auteur(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = f'Contact form submission from {name}'
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, email, fail_silently=False,)
        messages.success(request, 'Merci pour votre message ! Nous vous répondrons bientôt.')
    return render(request, 'LumenChristiilluminanos_app/auteur.html')

def augustin(request):
    return render(request, 'LumenChristiilluminanos_app/augustin.html')
def carlo(request):
    return render(request, 'LumenChristiilluminanos_app/carlo.html')
def giorgio(request):
    return render(request, 'LumenChristiilluminanos_app/giorgio.html')
def padrepio(request):
    return render(request, 'LumenChristiilluminanos_app/padrepio.html')
def tarcisius(request):
    return render(request, 'LumenChristiilluminanos_app/tarcisius.html')
def therese(request):
    return render(request, 'LumenChristiilluminanos_app/therese.html')
def rita(request):
    return render(request, 'LumenChristiilluminanos_app/rita.html')
def charbel(request):
    return render(request, 'LumenChristiilluminanos_app/charbel.html')