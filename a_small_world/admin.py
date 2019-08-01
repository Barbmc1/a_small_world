from django.contrib import admin

# Register your models here.
from  a_small_world.models import Products, Catagories, Manufacturers, Distributors
#from a_small_world.pieCharts import ManuPieChart

admin.site.register(Products)
admin.site.register(Catagories)
admin.site.register(Manufacturers)
admin.site.register(Distributors)
#admin.site.register(ManuPieChart)



