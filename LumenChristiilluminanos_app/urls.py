from . import views
from django.urls import path
app_name = 'LumenChristiilluminanos_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('prions/', views.prions, name='prions'),
    path('auteur/', views.auteur, name='auteur'),
]