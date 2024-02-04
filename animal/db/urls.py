from django.urls import path
from . import views

urlpatterns = [
    path('', views.db_home, name = 'db'),
    path('create', views.create, name='create'),
    path('results', views.db_home, name='results')
]