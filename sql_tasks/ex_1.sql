-- Создают данную таблицу.

CREATE TABLE product_prices (
	city VARCHAR(100),
	product VARCHAR,
	cost NUMERIC(10, 2), -- В задании целые числа,
	date DATE            -- я на всякий случай сделал с копейками
);