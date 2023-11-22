from core import views
from core.views import *
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('warning/', views.warning, name='404'),
    path('team/',views.team,name='team'),
    path('feature/',views.feature,name='feature'),
    path('appointment/',views.appointment,name='appointment'),
]