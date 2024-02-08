# Generated by Django 4.2.6 on 2024-02-05 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_alter_apartmentowner_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartmentowner',
            name='ownerBorn',
            field=models.CharField(max_length=20, verbose_name='Дата рождения владельца'),
        ),
        migrations.AlterField(
            model_name='family',
            name='checkDate',
            field=models.CharField(max_length=20, verbose_name='дата проверки'),
        ),
    ]