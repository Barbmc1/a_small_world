# a_small_world
A python/django project to show visualization of all things dollhouse!

The idea is to take the inventory list from my distributor, and brake the products down into
catagory_1, sub_catagory_1 and sub_catagory_2. For example:
          catagory_1 includes:
             Accessories
             Building components
             Furniture......
           
Under the catagory_1 is sub_catagory_1.  For the 
          sub_catagory_1 under catagoru_1 'Furniture' includes:
              Bedroom
              Bathroom
              Kitchen.....
             
Under the catagory_1 is the sub_catagory_2. For the 
          sub_catagory_2 under sub_catagory_1 'Bedroom' includes
              Bed
              Dresser
              night Stand.....
              
              
Each of the 3 levels of catagory/sub-catagory have pie-charts displaying the details of that catagory.

Ideally I would like for the program to have a file like charts.py that would use Pygal to generate the 
charts from the ProstreSQL Database that is linked to the project. However, I am not able to get the files
to run in Visual Studio, so I do not even know if I am on the right track iun creating charts.

I was able to make static Pie charts through the following steps:

Using the SQL queries from the charts.sql file I ran them in the pgAdmin app for PostgreSQL.  The first 3 queries, 
manufacturers, distributors and category_1, I was able to rewrite in PostgreSQL queries in the charts.py file. 
The 3 PostgreSQL I was able to successfully run in the Django shell.

The rest of the SQL queries I ran in the pgAdmin app for my PostgreSQL database. After running all queries, 
I copied and pasted the results into Microsoft Excel workbooks.  The  sub_catacory_1 and Sub_catagory_2 queries 
worked as planned, but did not fully give me the results I needed. But with Excel there was a simple but tedious 
fix. I copied and pasted category/subcategory onto its own spread sheet. Then Excel has a handy insert function 
that creates a pie chart from the data on the sheet. After formatting the chart, I was able to save an image of 
each chart. These images will have to be embedded in the templates.

This is NOT the way that I want to display this data in the app. I want to use queries, that then feed the data 
to pygal which will generate the charts.  

So this is where I am stuck in this project. I can't run the files in Visual Studio by going to 'Terminal' 
and clicking 'Run Active File.' I get an error stating that:
       (11_env) c:\Users\barbm\a_small_world$>c:\Users\barbm\a_small_world$\a_small_world\charts.py
        Traceback (most recent call last):
        File "C:\Users\barbm\a_small_world$\a_small_world\charts.py", line 6, in <module>
        from .models import Catagories, Manufacturers, Distributors, Products
        ModuleNotFoundError: No module named '__main__.models'; '__main__' is not a package
        
In other words, it does not have Django loaded. However, I am able to from the command line, pull the 
web site up, so I know that Django is loaded nd working. just won't work in the Visual Studio window.


             
