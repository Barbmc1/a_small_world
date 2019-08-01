import csv
import pygal
from pygal.style import DarkStyle
from pygal import Config


filename = 'a_small_world/prods_by_manufacturer.csv'

"""This will open and read the file, collecting all manufacturers & the number 
of Products thet sell. A Pie chart showing each manufacturers percent of the 
total products each manufacturer makes up."""
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	manufacturer_name, product_count = [], []
	for row in reader:
		manufacturer_name.append(row[0])
		
		product_count.append(row[1])
		
		
#Create Pie Chart
config = Config()
manuPie = pygal.Pie(config) 
manuPie.title = 'Products By Manufacturer'
manuPie.height=600
manuPie.width=800
manuPie.style=DarkStyle

manuPie.render_to_file('manuPieCsv.svg')



	
