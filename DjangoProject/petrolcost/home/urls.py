from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('deals/', views.deals, name='deals'),
    path('stats/', views.stats, name='stats'),
    path('contact/', views.contact, name='contact'),
    ]
