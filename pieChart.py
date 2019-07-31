import pygal
from pygal.style import DarkStyle

from .models import Catagories, Manufacturers, Distributors, Products
from django.db.models import Count


class ManuPieChart():
    def __init__(self, **kwargs):
        self.chart = pygal.Pie(**kwargs)
        self.chart.title = 'Products By Manufacturer'
        self.chart.height = 600
        self.chart.width = 800
        self.chart.explicit_size=True
        self.chart.style=DarkStyle


    def get_data(self):
        #m is a reverse query on the foreign key 'id' from Manufacturers 
        #to count the number of products by each manufacturer in the Products table.
        #This annotate method uses Count to return a query-set
        m = Manufacturers.objects.annotate(Count('products'))
        #Create a dictionary
        manuData = {}
        #Fill the dictionary by iterating over the m query-set
        for manufacturer in m.objects.all():
            manuData[manufacturer.name] = manufacturer.product__count
            return manuData

    def generate(self):
        #Get chart data
        chart_data = self.get_data()

        #Add data to chart
        for key, value in chart_data.items():
            self.chart.add(key, value)

        #Return the rendered svg as a string
        return self.chart.render(is_unicode=True)
        #Save the result to file
        self.chart.render_to_file('a_small_world/manuPie.svg')

        


    

