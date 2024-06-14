-- Самый дорогой товар по каждому городу 03.01.2024

SELECT city, product
FROM (
    SELECT 
		city, 
		product,
        ROW_NUMBER() OVER (
			PARTITION BY city ORDER BY cost DESC
		) AS max_cost
    FROM product_prices
    WHERE date = '2024-01-03'
) AS max_cost_by_city
WHERE max_cost = 1;