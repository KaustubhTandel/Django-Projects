from django.contrib import admin
from .models import Login
from .models import Personal_Informations
from .models import Car_Collections
from .models import Payment

# Register your models here.
admin.site.register(Login)
admin.site.register(Personal_Informations)
admin.site.register(Car_Collections)
admin.site.register(Payment)




