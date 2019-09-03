from django.db import models
from .models import Catagories, Manufacturers, Distributors, Products
from django.db.models import Count

import pygal
from pygal.style import DarkStyle
from pygal import Config


"""The following 3 queries, d, q, m all work. They have been 
tested in the django shell. The issue now is taken the query set &
feeding it to pygal to create a Pie chart. """

#This command line query works!
d = Distributors.objects.annotate(Count('products'))

#This command line query works! 
#Type q 'enter' to see the queryset <Catagories: DOLLS >,
#Type q[0].product__count  to see the number of products
q = Catagories.objects.annotate(Count('products'))



#This command line query works! 
#Open a command line and go to (11_env) C:\Users\barbm\a_small_world$>
#type manage.py shell   'enter'
#type from a_small_world.models import Products, Manufacturers  'enter'
#type from django.db.models import Count  'enter'
#type m = Manufacturers.objects.annotate(Count('products'))  'enter'
#Type m 'enter' to see the queryset <Manufacturers: McGhee's Miniatures >,
#Type m[0].product__count  to see the number of products
m = Manufacturers.objects.annotate(Count('products'))

manuData = {}

for manufacturer_name in m.objects.all():
   manuData[m.manufacturer_name] = m.product__count



config = Config()
manuPie = pygal.Pie(config) 
manuPie.title = 'Products By Manufacturer'
manuPie.height=600
manuPie.width=800
manuPie.style=DarkStyle
  

for k, v in manuData:
    manuPie.add(k, v)
manuPie.render_to_file('a_small_world/static/a_small_world/manuPie2.svg')







     


