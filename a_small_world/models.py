#from django.contrib.postgres.fields import ArrayField 
from django.db import models

# Create your models here.

class Products(models.Model):
    """Products are inventory items and include info about the manufacturer, distributer and the catagory as forein keys."""
    id = models.CharField(max_length=20, primary_key=True) 
    product_name = models.CharField(max_length=100)
    product_discription = models.TextField(max_length=00, null=True)
    price_value = models.FloatField(null=True)
    manufacturer = models.ForeignKey('Manufacturers', on_delete=models.CASCADE, null=True)
    catagories = models.ForeignKey('Catagories', on_delete=models.CASCADE, null=True)
    distributors = models.ForeignKey('Distributors', on_delete=models.CASCADE, null=True)

    #Without this line, the admin site lists Productss
    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        """Returns a string representation of the model."""
        return self.product_name

   
    
class Manufacturers(models.Model):
    """This table contains all information for a manufacturers and distributors."""
    id = models.IntegerField(primary_key=True)
    manufacturer_abv = models.CharField(max_length=4, null=True)
    manufacturer_name = models.CharField(max_length=50)
    manufacturer_sells = models.TextField(null=True)
    manufacturer_website = models.TextField(null=True)
    manufacturer_contact_first_name = models.CharField(max_length=15, null=True)
    manufacturer_contact_last_name = models.CharField(max_length=15, null=True)
    manufacturer_contact_title = models.CharField(max_length=15, null=True)
    manufacturer_address = models.CharField(max_length=50, null=True)
    manufacturer_city = models.CharField(max_length=25,null=True)
    manufacturer_state = models.CharField(max_length=15, null=True)
    manufacturer_zip_code = models.CharField(max_length=10,null=True)
    manufacturer_country = models.CharField(max_length=15,null=True)
    manufacturer_phone = models.CharField(max_length=15, null=True)
    manufacturer_email = models.CharField(max_length=50, null=True)
    manufacturer_notes = models.TextField(null=True)

    #Without this line, the admin site lists Manufacturerss
    class Meta:
        verbose_name_plural = 'Manufactuers'

    def __str__(self):
        """Return a string reprentation of the manufacturer."""
        return self.manufacturer_name



class Catagories(models.Model):
    """Contains catagories and sub-catagories for the products.."""
    id = models.IntegerField(primary_key=True)
    catagory_1 = models.CharField(max_length=35)
    sub_catagory_1 = models.CharField(max_length=35, null=True)
    sub_catagory_2 = models.CharField(max_length=50, null=True)
    HH = models.CharField(max_length=1, null =True)
    MM = models.CharField(max_length=1, null=True)

    #Without this line, the admin site lists Catagoriess
    class Meta:
        verbose_name_plural = 'Catagories'

    def __str__(self):
        """Return a string representing the catagory_1."""
        return self.catagory_1

               
#class Catagory_1(models.Model):
#    cat = models.Charfield(max_length=500)
#    key = models.ForeignKey('Catagories', on_delete=models.CASCADE)


#class CatArray(models.Model):
#    board = ArrayField(
#        ArrayField(
#            models.IntegerField(blank=True)
#        )
#    )


class Distributors(models.Model):
    """Contains the id for distributors."""
    id = models.IntegerField(primary_key=True)
    distributor_name = models.CharField(max_length=50)

    #Without this line, the admin site lists Distributorss
    class Meta:
        verbose_name_plural = 'Distributors'

    def __str__(self):
        """Return a string representation of the distrinutors name."""
        return self.distributor_name




class Catagory_1(models.Model):
    """This is the result of the query from products by catagory."""



