SELECT p.product_name,s.year,s.price
FROM Sales AS s 
INNER JOIN Product AS p
ON p.product_id = s.product_id;
-- SELECT product_name, year, price FROM Sales
-- JOIN Product
-- USING(product_id);
