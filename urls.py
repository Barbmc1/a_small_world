"""Define the URL patterns for a_small_world."""
from django.contrib import admin
from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'a_small_world'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),

    #Catagories page.
    path('catagories/', views.catagories, name='catagories'),

    #Manuifacturers page.
    path('manufacturers/', views.manufacturers, name='manufacturers'),

    #Distriutors page
    path('distributors/', views.distributors, name='distributors'),

    #Products page.
    path('products/', views.products, name='products'),

  

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)