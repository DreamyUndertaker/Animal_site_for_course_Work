# TODO реализовать формы для всех полей сущностей 

from django.forms import BooleanField, CharField, DateField, IntegerField, ModelForm

from animal.db.models import Apartment, ApartmentOwner, Entrance, Family, Pets


class ApartmentForm(ModelForm):
    class Meta:
        model = Apartment
        fields = {
            'entranceNumber', 
            'apartmentOwner',
            'familyId',
            'apartmentNumber',
            'roomNumber',
            'apartmentArea'
        }
        
        widgets = {
            'entranceNumber': IntegerField(attrs={
                'placeholder':'номер подъезда'
            }),
            'apartmentOwner': IntegerField(attrs={
                'placeholder':'номер владельца'
            }),
            'familyId': IntegerField(attrs={
                'placeholder':'номер семьи'
            }),
            'apartmentNumber': IntegerField(attrs={
                'placeholder':'номер квартиры'
            }),
            'roomNumber': IntegerField(attrs={
                'placeholder':'номер комнаты'
            }),
            'apartmentArea': IntegerField(attrs={
                'placeholder':'площадь комнаты'
            }),
        }

class FamilyForm(ModelForm):
    class Meta:
        model = Family
        fields = {
            'surname', 
            'checkDate',
            'phoneNumber',
        }
        widgets = {
            'surname': CharField (attrs={
                'placeholder':'фамилия семьи'
            }),
            'checkDate': DateField (attrs={
                'placeholder':'дата проверки'
            }),
            'phoneNumber': DateField (attrs={
                'placeholder':'номер телефона'
            }),
        }

class PetsForm(ModelForm):
    class Meta:
        model = Pets
        fields = {
            'familyId', 
            'petKind',
            'petNickname',
        }
        widgets = {
            'familyId': IntegerField (attrs={
                'placeholder':'номер семьи'
            }),
            'petKind': CharField (attrs={
                'placeholder':'вид питомца'
            }),
            'petNickname': CharField (attrs={
                'placeholder':'кличка питомца'
            }),
        }

class ApartmentOwnerForm(ModelForm):
    class Meta:
        model = ApartmentOwner
        fields = {
            'ownerName', 
            'ownerSurName',
            'ownerFatherName',
        }
        widgets = {
            'ownerName': CharField (attrs={
                'placeholder':'имя'
            }),
            'ownerSurName': CharField (attrs={
                'placeholder':'фамилия'
            }),
            'ownerFatherName': CharField (attrs={
                'placeholder':'отчество'
            }),
        }

class EntranceForm(ModelForm):
    class Meta:
        model = Entrance
        fields = {
            'entranceNumber', 
            'apartmentNumber',
            'floorNumber',
            'intercomAvailability',
        }
        widgets = {
            'entranceNumber': IntegerField (attrs={
                'placeholder':'номер подъезда'
            }),
            'apartmentNumber': IntegerField (attrs={
                'placeholder':'номер квартиры'
            }),
            'floorNumber': IntegerField (attrs={
                'placeholder':'номер этажа'
            }),
            'intercomAvailability': BooleanField (attrs={
                'placeholder':'домофон',
                
            }, required=True),
        }