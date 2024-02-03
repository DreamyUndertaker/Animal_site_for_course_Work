from django.contrib import admin

from .models import Apartment, ApartmentOwner, Entrance, Family, Pets

# Register your models here.
admin.site.register(Apartment)
admin.site.register(Family)
admin.site.register(Pets)
admin.site.register(ApartmentOwner)
admin.site.register(Entrance)
