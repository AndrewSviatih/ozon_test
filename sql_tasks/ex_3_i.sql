-- *Укажите ежедневную динамику 
-- количества ассортимента сети магазинов


-- Если я правильно понял, нужно кол-во уникальных товаров.

SELECT
    date,
    COUNT(DISTINCT product) AS product_count
FROM product_prices
GROUP BY date
ORDER BY date;