SELECT *
FROM products;

SELECT sum(product_id) as shampoo
FROM products
GROUP BY low_fats
HAVING product_id % 2 = 0;