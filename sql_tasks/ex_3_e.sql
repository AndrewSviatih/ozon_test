-- Товары, которые продавались в Кирове, но не продавались в Москве

(
    SELECT product
    FROM product_prices
    WHERE city = 'Киров'
)
EXCEPT
(
    SELECT product
    FROM product_prices
    WHERE city = 'Москва'
);

-- Еще можно использовать NOT IN с вложенным запросом,
-- но он будет менее эффективным, т.к.
-- подзапрос будет выполняться для каждой строки