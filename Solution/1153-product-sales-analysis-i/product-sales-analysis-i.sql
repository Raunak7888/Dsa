-- select t1.product_name,t2.year,t2.price
-- from Sales as t2 
-- INNER join Product as t1
-- on t1.product_id = t2.product_id;
SELECT product_name, year, price FROM Sales
JOIN Product
USING(product_id);
