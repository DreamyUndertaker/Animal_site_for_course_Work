from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
# from .models import Articles, Persons, Deposites, ExchangeRates, Clients, DepositsRegistration
# from .forms import ArticleForm, ClientsForm, DepositesForm, DepositsRegistrationForm, ExchangeRatesForm, PersonsForm

# Create your views here.
def db_home(request):
    # db = Articles.objects.all()
    # db1 = Persons.objects.all()
    # db2 = Deposites.objects.all()
    # db3 = ExchangeRates.objects.all()
    # db4 = Clients.objects.all()
    # db5 = DepositsRegistration.objects.all()
    return render(request, 'db/db.html', )