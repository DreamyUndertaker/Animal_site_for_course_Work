from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration, name = 'registration'),
    path('singin', views.signin, name='signin'),
    path('home', views.home, name='home'),
]