-- **Укажите по каждому товару среднюю динамику 
-- изменения цены по каждому городу за все время работы сети магазинов

-- Как я понял задачу:
-- Нужно найти среднее изменение значения цены city + product по всем датам

-- Находим предыдущую стоимость товара
-- с помощью LAG по city, product и date
WITH cost_changes AS (
	SELECT
		city,
		product,
		date,
		cost,
		LAG (cost) OVER (
			PARTITION BY city, product
			ORDER BY date
		) AS prev_cost
	FROM product_prices
),
-- находим разницу цены между текущим и прошлым днем
cost_differences AS (
	SELECT
		city,
		product,
		date,
		cost,
		(cost - prev_cost) AS cost_change
	FROM cost_changes
	WHERE prev_cost IS NOT NULL -- Пропускаем первые вхождения цены
)

-- находим среднее изменение цены
SELECT 
	city,
	product,
	ROUND(AVG(cost_change), 2) AS avg_cost_changes
FROM cost_differences
GROUP BY city, product
ORDER BY city, product;