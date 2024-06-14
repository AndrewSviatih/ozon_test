-- По каждому городу количество продуктов, продаваемых 02.01.2024.

SELECT
	city,
	COUNT(product) AS product_count
FROM product_prices
WHERE date = '2024-01-02'
GROUP BY city;