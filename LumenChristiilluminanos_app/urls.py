from . import views
from django.urls import path
app_name = 'LumenChristiilluminanos_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('prions/', views.prions, name='prions'),
    path('auteur/', views.auteur, name='auteur'),
    path('augustin/', views.augustin, name='augustin'),
    path('carlo/', views.carlo, name='carlo'),
    path('giorgio/', views.giorgio, name='giorgio'),
    path('padrepio/', views.padrepio, name='padrepio'),
    path('tarcisius/', views.tarcisius, name='tarcisius'),
    path('therese/', views.therese, name='therese'),
    path('rita/', views.rita, name='rita'),
    path('charbel/', views.charbel, name='charbel'),
]