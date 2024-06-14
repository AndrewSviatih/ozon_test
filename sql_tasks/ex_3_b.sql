-- Минимальную стоимость каждого товара за все время работы сети магазинов

SELECT
	product,
	MIN(cost)
FROM product_prices
GROUP BY product;