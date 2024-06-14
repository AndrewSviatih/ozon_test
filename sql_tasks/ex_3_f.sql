-- Среднюю цену каждого товара на каждый день в сети магазинов

SELECT
    product,
    date,
    ROUND(AVG(cost), 2) AS avg_cost
FROM product_prices
GROUP BY product, date;