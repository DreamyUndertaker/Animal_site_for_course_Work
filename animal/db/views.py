from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from .forms import ApartmentForm, ApartmentOwnerForm, EntranceForm, FamilyForm, PetsForm

from .models import Apartment, ApartmentOwner, Entrance, Family, Pets


# Create your views here.
def db_home(request):
    db = Apartment.objects.all()
    db1 = Family.objects.all()
    db2 = Pets.objects.all()
    db3 = ApartmentOwner.objects.all()
    db4 = Entrance.objects.all()
    return render(request, 'db/db.html', {'Apartment' : db, 'Family': db1, 'Pets' : db2, 'ApartmentOwner': db3, 'Entrance': db4})

def create(request):
    error = ''
    if request.method == 'POST':
        apartmentForm = ApartmentForm(request.POST)
        familyForm = FamilyForm(request.POST)
        petsForm = PetsForm(request.POST)
        apartmentOwnerForm = ApartmentOwnerForm(request.POST)
        entranceForm = EntranceForm(request.POST)
        if apartmentOwnerForm.is_valid():
            apartmentForm.save()
            familyForm.save()
            petsForm.save()
            entranceForm.save()
            apartmentOwnerForm.save()
            return redirect('results')
        else:
            error = "форма была не верной"
    apartmentForm = ApartmentForm()
    familyForm = FamilyForm()
    petsForm = PetsForm()
    apartmentOwnerForm = ApartmentOwnerForm()
    entranceForm = EntranceForm()
    data = {
        'apartmentForm': apartmentForm,
        'familyForm': familyForm,
        'petsForm': petsForm,
        'apartmentOwnerForm': apartmentOwnerForm,
        'entranceForm': entranceForm,
        'error': error 
    }
    return render(request, 'db/create.html', data)