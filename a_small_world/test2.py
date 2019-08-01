import pygal

from pygal.style import DarkStyle
from pygal import Config

#from .models import Catagories, Manufacturers, Distributors, Products
#from django.db.models import Count

config = Config()


manuPie = pygal.Pie(config)
manuPie.title = 'Products By Manufacturer'
manuPie.height=600
manuPie.width=800
manuPie.style=DarkStyle

#manuPie.add([manufacturer_name], [product_count])

#I added these hard code values to see if the chart would ender. It doesn't.
manuPie.add('McGhees Miniatures ', 1600)
manuPie.add('Classics-Handley House', 831) 
manuPie.add('Aztec', 3421)
manuPie.add('Dee Delight', 77)  
manuPie.add('Chrysnbon', 315)
manuPie.add('Barbara OBrien', 139)
manuPie.add('Cir-Kit Concepts ', 365)


#return manuPie.render(is_unicode=True)
manuPie.render_to_file('static/a_small_world/manuPie.svg')
