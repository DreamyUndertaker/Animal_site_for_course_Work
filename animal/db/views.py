from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import ApartmentForm, ApartmentOwnerForm, EntranceForm, FamilyForm, PetsForm
from .models import Apartment, ApartmentOwner, Entrance, Family, Pets

# получение данных из бд
def db_home(request):
    apartment = Apartment.objects.all()
    family = Family.objects.all()
    pets = Pets.objects.all()
    apartmentOwner = ApartmentOwner.objects.all()
    entrance = Entrance.objects.all()
    return render(request, 'db/db.html', {'Apartment' : apartment, 
                                            'Family': family, 
                                            'Pets' : pets, 
                                            'ApartmentOwner': apartmentOwner, 
                                            'Entrance': entrance})

# со[ранение данных в бд
def create(request):
    error = ''
    if request.method == 'POST':
        apartmentForm = ApartmentForm(request.POST)
        familyForm = FamilyForm(request.POST)
        petsForm = PetsForm(request.POST)
        apartmentOwnerForm = ApartmentOwnerForm(request.POST)
        entranceForm = EntranceForm(request.POST)
        if apartmentOwnerForm.is_valid():
            
            apartmentForm.entranceNumber = request.POST.get('entranceNumber')
            apartmentForm.apartmentOwner = request.POST.get('apartmentOwner')
            apartmentForm.familyId = request.POST.get('familyId')
            apartmentForm.apartmentNumber = request.POST.get('apartmentNumber')
            apartmentForm.roomNumber = request.POST.get('roomNumber')
            apartmentForm.apartmentArea = request.POST.get('apartmentArea')
            apartmentForm.save()

            
            familyForm.save()
            petsForm.save()
            entranceForm.save()
            apartmentOwnerForm.save()
            return HttpResponseRedirect('')
        else:
            error = "форма была не верной"

def edit(request, id):
    try:

        if request.method == "POST":
            apartmentForm = ApartmentForm(request.POST)
            familyForm = FamilyForm(request.POST)
            petsForm = PetsForm(request.POST)
            apartmentOwnerForm = ApartmentOwnerForm(request.POST)
            entranceForm = EntranceForm(request.POST)
            return render(request, 'db/db.html', {'Apartment' : apartment, 
                                            'Family': family, 
                                            'Pets' : pets, 
                                            'ApartmentOwner': apartmentOwner, 
                                            'Entrance': entrance})
    except :
        return HttpResponseNotFound("<h2>DB not found</h2>")