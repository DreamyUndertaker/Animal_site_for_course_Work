# Generated by Django 4.2.6 on 2024-02-03 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entranceNumber', models.IntegerField(verbose_name='номер подъезда')),
                ('apartmentOwner', models.IntegerField(verbose_name='номер владельца квартиры')),
                ('familyId', models.IntegerField(verbose_name='номер семьи')),
                ('apartmentNumber', models.IntegerField(verbose_name='номер квартиры')),
                ('roomNumber', models.IntegerField(verbose_name='номер комнаты')),
                ('apartmentArea', models.IntegerField(verbose_name='площадь комнаты')),
            ],
            options={
                'verbose_name': 'квартира',
                'verbose_name_plural': 'квртиры',
            },
        ),
        migrations.CreateModel(
            name='ApartmentOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ownerName', models.TextField(verbose_name='Имя владельца')),
                ('ownerSurName', models.TextField(verbose_name='Фамилия владельца')),
                ('ownerFatherName', models.TextField(verbose_name='Отчество владельца')),
                ('ownerBorn', models.DateField(verbose_name='Дата рождения владельца')),
                ('phoneNumber', models.CharField(max_length=20, verbose_name='номер телефона')),
            ],
            options={
                'verbose_name': 'Владелец квртиры',
                'verbose_name_plural': 'Владельцы квартиры',
            },
        ),
        migrations.CreateModel(
            name='Entrance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entranceNumber', models.IntegerField(verbose_name='номер подъезда')),
                ('apartmentNumber', models.IntegerField(verbose_name='номер квартиры')),
                ('floorNumber', models.IntegerField(verbose_name='номер этажа')),
                ('intercomAvailability', models.BooleanField(verbose_name='наличие домофона')),
            ],
            options={
                'verbose_name': 'Подъезд',
                'verbose_name_plural': 'Подъезды',
            },
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.TextField(verbose_name='Фамилия')),
                ('checkDate', models.DateField(verbose_name='дата проверки')),
                ('phoneNumber', models.CharField(max_length=20, verbose_name='номер телефона')),
            ],
            options={
                'verbose_name': 'семья',
                'verbose_name_plural': 'семьи',
            },
        ),
        migrations.CreateModel(
            name='Pets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('familyId', models.IntegerField(verbose_name='номер семьи')),
                ('petKind', models.TextField(verbose_name='Вид питомца')),
                ('petNickname', models.TextField(verbose_name='Кличка питомца')),
            ],
            options={
                'verbose_name': 'Питомцы',
                'verbose_name_plural': 'Питомцы',
            },
        ),
    ]