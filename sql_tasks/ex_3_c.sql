-- Среднюю цену всего ассортимента товаров по каждому городу на каждый день

SELECT
    city,
    date,
    ROUND(AVG(cost), 2) AS avg_cost
FROM product_prices
GROUP BY city, date;
-- Здесь еще бы сделал сортировку по city и date