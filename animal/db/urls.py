from django.urls import path
from . import views

urlpatterns = [
    path('', views.db_home, name = 'db'),
    path('create/', views.create, name='create'),
    path('<int:pk>', views.PersonDetailView.as_view(), name='person-detail'),
    path('<int:pk>/update', views.PersonUpdateView.as_view(), name='person-update'),

]             