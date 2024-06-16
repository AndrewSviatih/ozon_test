-- По каждому товару вывести город, в котором он был самым дорогим

SELECT
    product,
    city
FROM (
    SELECT 
        product,
        city,
        ROW_NUMBER() OVER (
			PARTITION BY product 
            ORDER BY cost DESC
		) AS max_cost
    FROM product_prices
) 
WHERE max_cost = 1;