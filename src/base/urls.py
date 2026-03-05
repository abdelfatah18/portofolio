from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('portfolio', views.portfolio, name='indportfolio'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('portfolio-details', views.portfolio_details, name='portfolio'),
    path('services-details', views.services_details, name='services-details'),
    path('resume', views.resume, name='resume'),
    path('starter', views.starter, name='starter'),
    
]
