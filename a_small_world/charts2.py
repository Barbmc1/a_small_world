from django.db import models
import pygal
from pygal.style import DarkStyle
from pygal import Config

from .models import Catagories, Manufacturers, Distributors, Products
from django.db.models import Count


#This command line query works! 
#Type q 'enter' to see the queryset <Catagories: DOLLS >,
#Type q[0].product__count  to see the number of products
q = Catagories.objects.annotate(Count('products'))



#This command line query works! 
#Type m 'enter' to see the queryset <Manufacturers: McGhee's Miniatures >,
#Type m[0].products__count  to see the number of products
m = Manufacturers.objects.annotate(Count('products'))

manu_dict = m

name, num = [], []

for info in m.objects.all():
   name.append(m['manufacturer_name'])
   num.append(m['product__count'])

config = Config()
manuPie = pygal.Pie(config)
manuPie.title = 'Products By Manufacturer'
manuPie.height=600
manuPie.width=800
manuPie.style=DarkStyle

manuPie.add(name, num)
manuPie.render_to_file('a_small_world/static/a_small_world/manuPie3.svg')



d = Distributors.objects.annotate(Count('products'))


     


