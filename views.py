import pygal
from django.views.generic import TemplateView
from pygal.style import DarkStyle

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Catagories, Manufacturers, Distributors, Products
from .pieChart import ManuPieChart

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required




def index(request):
    """The home page for a_small_world."""
    return render(request, 'a_small_world/index.html')

 
def catagories(request):
    """The web page for product catagories."""
    catagory_1 = Catagories.objects.order_by('catagory_1').distinct('catagory_1')
    context = {'catagory_1': catagory_1}
    return render(request, 'a_small_world/catagories.html', context)



def manufacturers(request):
    """The web page for product manufacturers."""
    manufacturer_name = Manufacturers.objects.order_by('manufacturer_name').distinct('manufacturer_name')
    context = {'manufacturer_name': manufacturer_name}
    return render(request, 'a_small_world/manufacturers.html', context)
    return render(request, 'a_small_world/manuPie.svg', context)


def distributors(request):
    """This web page is for the disrtibutiors."""
    distributor_name = Distributors.objects.order_by('distributor_name').distinct('distributor_name')
    context = {'distributor_name': distributor_name}
    return render(request, 'a_small_world/distributors.html', context)


def products(request):
    """This is the products page."""
    product_name = Products.objects.order_by('catagories')
    context = {'product_name': product_name}
    return render(request, 'a_small_world/products.html', context)

def manuPie(request):
    """This is to display the pygal chart."""
    manuPie = ManuPieChart(
        height = 600,
        width = 800,
        explicit_size=True,
        style=DarkStyle
    )
    context = context['manuPie'] = manuPie.generate()
    context.render_to_file('/a_small_world/manuPie.svg')
    return render(request, 'a_small_world/manufacturers.html', context)