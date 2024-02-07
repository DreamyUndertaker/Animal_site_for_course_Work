# TODO реализовать формы для всех полей сущностей 

from django.forms import CheckboxInput, DateInput, TextInput, DateTimeInput, NumberInput, ModelForm

from .models import Apartment, ApartmentOwner, Entrance, Family, Pets


class ApartmentForm(ModelForm):
    class Meta:
        model = Apartment
        fields = [
            'entranceNumber', 
            'apartmentOwner',
            'familyId',
            'apartmentNumber',
            'roomNumber',
            'apartmentArea'
        ]
        widgets = {
            "entranceNumber": NumberInput(attrs={
                'placeholder':'номер подъезда'
            }),
            "apartmentOwner": NumberInput(attrs={
                'placeholder':'номер владельца'
            }),
            "familyId": NumberInput(attrs={
                'placeholder':'номер семьи'
            }),
            "apartmentNumber": NumberInput(attrs={
                'placeholder':'номер квартиры'
            }),
            "roomNumber": NumberInput(attrs={
                'placeholder':'номер комнаты'
            }),
            "apartmentArea": NumberInput(attrs={
                'placeholder':'площадь комнаты'
            }),
        }

class FamilyForm(ModelForm):
    class Meta:
        model = Family
        fields = [
            'surname', 
            'checkDate',
            'phoneNumber',
        ]
        widgets = {
            "surname": TextInput(attrs={
                'placeholder':'фамилия семьи'
            }),
            "checkDate": DateInput(attrs={
                
            }),
            "phoneNumber": NumberInput(attrs={
                
            }),
        }

class PetsForm(ModelForm):
    class Meta:
        model = Pets
        fields = [
            'familyId', 
            'petKind',
            'petNickname',
        ]
        widgets = {
            "familyId": NumberInput(attrs={
                'placeholder':'номер семьи'
            }),
            "petKind": TextInput(attrs={
                'placeholder':'вид питомца'
            }),
            "petNickname": TextInput(attrs={
                'placeholder':'кличка питомца'
            }),
        }

class ApartmentOwnerForm(ModelForm):
    class Meta:
        model = ApartmentOwner
        fields = [
            'ownerName', 
            'ownerSurName',
            'ownerFatherName',
            'ownerBorn',
            'phoneNumber',
        ]
        widgets = {
            "ownerName": TextInput(attrs={
                'placeholder':'имя'
            }),
            "ownerSurName": TextInput(attrs={
                'placeholder':'фамилия'
            }),
            "ownerFatherName": TextInput(attrs={
                'placeholder':'отчество'
            }),
            "ownerBorn": TextInput(attrs={
                
            }),
            "phoneNumber": TextInput(attrs={
                'placeholder':'phoneNumber'
            }),

        }

class EntranceForm(ModelForm):
    class Meta:
        model = Entrance
        fields = [
            'entranceNumber', 
            'apartmentNumber',
            'floorNumber',
            'intercomAvailability',
        ]
        widgets = {
            "entranceNumber": NumberInput(attrs={
                'placeholder':'номер подъезда'
            }),
            "apartmentNumber": NumberInput(attrs={
                'placeholder':'номер квартиры'
            }),
            "floorNumber": NumberInput(attrs={
                'placeholder':'номер этажа'
            }),
            "intercomAvailability": CheckboxInput (attrs={
                'placeholder':'домофон',
                
            }),
        }