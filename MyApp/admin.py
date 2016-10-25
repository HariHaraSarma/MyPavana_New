from django.contrib import admin

# Register your models here.
from MyApp.models import Person, ComplteStockDetails, DealersInfo
admin.site.register(Person)
admin.site.register(DealersInfo)
admin.site.register(ComplteStockDetails)