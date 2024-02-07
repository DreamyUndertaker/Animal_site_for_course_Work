from django.views.generic import DetailView, UpdateView
from django.shortcuts import redirect, render
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

class PersonDetailView(DetailView):
    model = ApartmentOwner 
    
    def get_context_data(self,*args, **kwargs):
        print(self.__dir__)    
        context = super(PersonDetailView, self).get_context_data(*args,**kwargs)
        
        context['entrance'] = Entrance.objects.get(self.request)
        context['apartment'] = Apartment.objects.get(self.request)
        context['family'] = Family.objects.get(self.request)
        context['pets'] = Pets.objects.get(self.request)
        return context
        
    template_name = 'db/details_view.html'
    context_object_name = 'apartmentOwner'
    

    
    

class PersonUpdateView(UpdateView):
    model = ApartmentOwner

    template_name = 'db/create.html'
    context_object_name = 'apartmentOwner'

    form_class = ApartmentOwnerForm


# сохранение данных в бд
def create(request):
    error = ''
    if request.method == 'POST':
        apartmentForm = ApartmentForm(request.POST)
        familyForm = FamilyForm(request.POST)
        petsForm = PetsForm(request.POST)
        apartmentOwnerForm = ApartmentOwnerForm(request.POST)
        entranceForm = EntranceForm(request.POST)
        if apartmentOwnerForm.is_valid() and familyForm.is_valid() and petsForm.is_valid() and apartmentForm.is_valid() and entranceForm.is_valid():
            apartmentForm.save()
            familyForm.save()
            petsForm.save()
            entranceForm.save()
            apartmentOwnerForm.save()
            return redirect('db')
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


