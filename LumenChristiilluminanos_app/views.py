from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'LumenChristiilluminanos_app/index.html')

def about(request):
    return render(request, 'LumenChristiilluminanos_app/about.html')

def prions(request):
    return render(request, 'LumenChristiilluminanos_app/prions.html')

def auteur(request):
    return render(request, 'LumenChristiilluminanos_app/auteur.html')