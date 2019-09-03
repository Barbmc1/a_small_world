/*I am able to use these SQL queries in the pgAdmin app for the postgrsql.
There they return the desired results from my database. The first 3 queries, 
manufactures, distributors, and catagory_1, I was able to write postresql queries
which are located the charts.py file.  I know these queries work because I tested 
them in the dgjango shell. 

/*Working manufacturers query*/
SELECT a_small_world_manufacturers.manufacturer_name, COUNT(*)
    FROM a_small_world_products
    INNER JOIN a_small_world_manufacturers
    ON a_small_world_manufacturers.id =a_small_world_products.manufacturer_id 
    GROUP BY a_small_world_manufacturers.manufacturer_name
	ORDER BY a_small_world_manufacturers.manufacturer_name

/*Working distributors query.*/
SELECT a_small_world_distributors.distributor_name, COUNT(*)
    FROM a_small_world_products
    INNER JOIN a_small_world_distributors
    ON a_small_world_products.distributors_id = a_small_world_distributors.id
    GROUP BY a_small_world_distributors.distributor_name
    ORDER BY a_small_world_distributors.distributor_name

/*Working for catagory_1 count.*/
SELECT catagory_1, COUNT(*)
    FROM a_small_world_products
    INNER JOIN a_small_world_catagories
    ON a_small_world_products.catagories_id = a_small_world_catagories.id
    GROUP BY catagory_1
    ORDER BY catagory_1


/*The following two queries work, but there is a problem. I want to use the 
results of the queries to create pie charts to show greater detail for the 
catagory abve the one being detailed. This query result returns ALL the 
sub-catatgories of ALL the catagories above it. I need each catagory and sub-catagory 
to be it's query set or result. I either have to parse the queryt set results
to get the different catagories, or I have to create sepperate queries for each 
catagory andd sub-catagpry. */

/*This works to get the subcatagory_1 count.*/
SELECT catagory_1, sub_catagory_1, COUNT(*)
    FROM a_small_world_products
    INNER JOIN a_small_world_catagories
    ON a_small_world_products.catagories_id = a_small_world_catagories.id
	GROUP BY catagory_1, sub_catagory_1
    ORDER BY catagory_1, sub_catagory_1


/*This works to get the sub_catagory_2 count. */
SELECT catagory_1, sub_catagory_1, sub_catagory_2, COUNT(*)
    FROM a_small_world_products
    INNER JOIN a_small_world_catagories
    ON a_small_world_products.catagories_id = a_small_world_catagories.id
	GROUP BY catagory_1, sub_catagory_1, sub_catagory_2
    ORDER BY catagory_1, sub_catagory_1, sub_catagory_2




/************************************************************************************/

/*This quesry attempts to get the count of sub_catagory_1 when the catagory = ACCESSORIES */
SELECT a_small_world_catagories.sub_catagory_1, COUNT(*)
    FROM a_small_world_products
    WHERE a_small_world_catagories.catagory_1 IN 
        (SELECT a_small_world_catagories.catagory_1
        FROM a_small_world_catagories
        WHERE a_small_world_catagories.catagory_1 = ACCESSORIES)
    GROUP BY a_small_world_catagories.sub_catagory_1
    ORDER BY a_small_world_catagories.sub_catagory_1 


