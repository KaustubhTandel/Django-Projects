from django.contrib import admin
from MyApp.models import Personal_Details
from .models import Favourite_Details
from .models import Address_Details
from .models import Skills_Details

# Register your models here.
admin.site.register(Personal_Details)
admin.site.register(Favourite_Details)
admin.site.register(Address_Details)
admin.site.register(Skills_Details)
