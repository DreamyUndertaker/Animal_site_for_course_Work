from django.db import models

# Create your models here.
class Apartment(models.Model):
    entranceNumber = models.IntegerField('номер подъезда')
    apartmentOwner = models.IntegerField('номер владельца квартиры')
    familyId = models.IntegerField('номер семьи')
    apartmentNumber = models.IntegerField('номер квартиры')
    roomNumber = models.IntegerField('номер комнаты')
    apartmentArea = models.IntegerField('площадь комнаты')

    def get_absolute_url(self):
        return f'/db/{self.id}'

    def __str__(self):
        return f'Квартира:'
    class Meta:
        verbose_name = 'квартира'
        verbose_name_plural = 'квртиры'

class Family(models.Model):
    surname = models.TextField('Фамилия')
    checkDate = models.CharField('дата проверки', max_length=20)
    phoneNumber = models.CharField('номер телефона', max_length=20)

    def get_absolute_url(self):
        return f'/db/{self.id}'

    def __str__(self):
        return f'Семья:'
    class Meta:
        verbose_name = 'семья'
        verbose_name_plural = 'семьи'

class Pets(models.Model):
    familyId = models.IntegerField('номер семьи')
    petKind = models.TextField('Вид питомца')
    petNickname = models.TextField('Кличка питомца')

    def get_absolute_url(self):
        return f'/db/{self.id}'

    def __str__(self):
        return f'Питомцы:'
    class Meta:
        verbose_name = 'Питомцы'
        verbose_name_plural = 'Питомцы'

class ApartmentOwner(models.Model):
    ownerName = models.TextField('Имя владельца')
    ownerSurName = models.TextField('Фамилия владельца')
    ownerFatherName = models.TextField('Отчество владельца')
    ownerBorn = models.CharField('Дата рождения владельца', max_length=20)
    phoneNumber = models.CharField('номер телефона', max_length=20)

    def get_absolute_url(self):
        return f'/db/{self.id}'

    def __str__(self):
        return f'Владелец квартиры:'
    class Meta:
        verbose_name = 'Владелец квртиры'
        verbose_name_plural = 'Владельцы квартиры'

class Entrance(models.Model):
    entranceNumber = models.IntegerField('номер подъезда')
    apartmentNumber = models.IntegerField('номер квартиры')
    floorNumber = models.IntegerField('номер этажа')
    intercomAvailability = models.BooleanField('наличие домофона')

    def get_absolute_url(self):
        return f'/db/{self.id}'

    def __str__(self):
        return f'Подъезд: '
    class Meta:
        verbose_name = 'Подъезд'
        verbose_name_plural = 'Подъезды'
