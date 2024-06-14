-- Сколько товаров продается ежедневно в сети магазинов.
-- И сколько уникальных.

SELECT 
    date,
    COUNT(*) AS total_products,
    COUNT(DISTINCT Product) AS unique_products
FROM product_prices
GROUP BY date
ORDER BY date;