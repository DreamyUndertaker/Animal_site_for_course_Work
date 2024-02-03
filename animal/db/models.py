from django.db import models

# Create your models here.
class Apartment(models.Model):
    entranceNumber = models.IntegerField('номер подъезда')
    apartmentOwner = models.IntegerField('номер владельца квартиры')
    familyId = models.IntegerField('номер семьи')
    apartmentNumber = models.IntegerField('номер квартиры')
    roomNumber = models.IntegerField('номер комнаты')
    apartmentArea = models.IntegerField('площадь комнаты')

    def __str__(self):
        return f'Квартира: {self.title}'
    class Meta:
        verbose_name = 'квартира'
        verbose_name_plural = 'квртиры'

class Family(models.Model):
    surname = models.TextField('Фамилия')
    checkDate = models.DateField('дата проверки')
    phoneNumber = models.CharField('номер телефона', max_length=20)

    def __str__(self):
        return f'Семья: {self.title}'
    class Meta:
        verbose_name = 'семья'
        verbose_name_plural = 'семьи'

class Pets(models.Model):
    familyId = models.IntegerField('номер семьи')
    petKind = models.TextField('Вид питомца')
    petNickname = models.TextField('Кличка питомца')

    def __str__(self):
        return f'Питомцы: {self.title}'
    class Meta:
        verbose_name = 'Питомцы'
        verbose_name_plural = 'Питомцы'

class ApartmentOwner(models.Model):
    ownerName = models.TextField('Имя владельца')
    ownerSurName = models.TextField('Фамилия владельца')
    ownerFatherName = models.TextField('Отчество владельца')

    ownerBorn = models.DateField('Дата рождения владельца')
    phoneNumber = models.CharField('номер телефона', max_length=20)

    def __str__(self):
        return f'Владелец квартиры: {self.title}'
    class Meta:
        verbose_name = 'Владелец квртиры'
        verbose_name_plural = 'Владельцы квартиры'

class Entrance(models.Model):
    entranceNumber = models.IntegerField('номер подъезда')
    apartmentNumber = models.IntegerField('номер квартиры')
    floorNumber = models.IntegerField('номер этажа')
    intercomAvailability = models.BooleanField('наличие домофона')

    def __str__(self):
        return f'Подъезд: {self.title}'
    class Meta:
        verbose_name = 'Подъезд'
        verbose_name_plural = 'Подъезды'
