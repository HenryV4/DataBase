-- 1
SELECT maker, type
FROM lab2.Product
WHERE type = 'PC'
ORDER BY maker DESC;

-- 2
SELECT DISTINCT date
FROM lab2.Pass_in_trip
WHERE place LIKE '%c';

-- 3
SELECT p.name, pit.date
FROM lab2.Passenger p
JOIN lab2.Pass_in_trip pit ON p.ID_psg = pit.ID_psg
ORDER BY p.name, pit.date;

-- 4

START TRANSACTION;
USE lab2;
INSERT INTO lab2.Classes (`class`, `type`, `country`, `numGuns`, `bore`, `displacement`) 
VALUES ('Hetman Sahaidachny', 'fr', 'Ukraine', 1, 3.0, 3200)
ON DUPLICATE KEY UPDATE `type` = 'fr', `country` = 'Ukraine', `numGuns` = 1, `bore` = 3.0, `displacement` = 3200;
INSERT INTO lab2.Ships (`name`, `class`, `launched`) 
VALUES ('Hetman Sahaidachny', 'Hetman Sahaidachny', 1993)
ON DUPLICATE KEY UPDATE `launched` = 1993;
COMMIT;

-- Select rows for Ukraine if they exist
SELECT country, class
FROM lab2.Classes
WHERE country = 'Ukraine'
UNION
-- Only execute this if Ukraine is NOT found in any row
SELECT country, class
FROM lab2.Classes
WHERE NOT EXISTS (SELECT * FROM lab2.Classes WHERE country = 'Ukraine');

START TRANSACTION;
USE lab2;
DELETE FROM lab2.Ships
WHERE name = 'Hetman Sahaidachny';
DELETE FROM lab2.Classes
WHERE class = 'Hetman Sahaidachny';
COMMIT;

-- Select rows for Ukraine if they exist
SELECT country, class
FROM lab2.Classes
WHERE country = 'Ukraine'
UNION
-- Only execute this if Ukraine is NOT found in any row
SELECT country, class
FROM lab2.Classes
WHERE NOT EXISTS (SELECT * FROM lab2.Classes WHERE country = 'Ukraine');


-- 5
SELECT DISTINCT maker
FROM lab2.Product
WHERE type = 'Laptop'
AND maker NOT IN (
	SELECT maker
    FROM lab2.Product
    WHERE type = 'PRINTER'
);

-- 6
SELECT 
  CONCAT('модель: ', code) AS code_info,
  CONCAT('колір: ', color) AS color_info,
  CONCAT('тип: ', type) AS type_info,
  CONCAT('ціна: ', price) AS price_info,
  CONCAT('модель продукту: ', model) AS model_info
FROM lab2.Printer;

-- 7
WITH CountryYearShipCount AS (
    SELECT c.country, s.launched AS year, COUNT(s.name) AS ship_count
    FROM lab2.Classes c
    JOIN lab2.Ships s ON c.class = s.class
    GROUP BY c.country, s.launched
),
MaxShipCountPerCountry AS (
    SELECT country, MAX(ship_count) AS max_ship_count
    FROM CountryYearShipCount
    GROUP BY country
)
SELECT c.country, c.ship_count, c.year
FROM CountryYearShipCount c
JOIN MaxShipCountPerCountry m 
    ON c.country = m.country 
    AND c.ship_count = m.max_ship_count
WHERE c.year = (
    SELECT MIN(year)
    FROM CountryYearShipCount
    WHERE country = c.country
    AND ship_count = m.max_ship_count
);

-- 8
SELECT 
    p.maker,
    (SELECT COUNT(*) FROM lab2.PC pc WHERE pc.model IN (
    SELECT model FROM lab2.Product WHERE maker = p.maker
    )) AS pc,
    (SELECT COUNT(*) FROM lab2.Laptop l WHERE l.model IN (
    SELECT model FROM lab2.Product WHERE maker = p.maker
    )) AS laptop,
    (SELECT COUNT(*) FROM lab2.Printer pr WHERE pr.model IN (
    SELECT model FROM lab2.Product WHERE maker = p.maker
    )) AS printer
FROM 
    lab2.Product p
GROUP BY 
    p.maker;

-- 9
SELECT maker,
    CASE
        WHEN (SELECT COUNT(*) FROM lab2.Laptop l JOIN lab2.Product p ON l.model = p.model WHERE p.maker = pr.maker) > 0
			THEN CONCAT('yes(', (SELECT COUNT(*) FROM lab2.Laptop l JOIN lab2.Product p ON l.model = p.model WHERE p.maker = pr.maker), ')')
        ELSE 'no'
    END AS laptop
FROM lab2.Product pr
GROUP BY maker;

-- 10
SELECT class
FROM lab2.Ships
GROUP BY class
HAVING COUNT(name) = 1

UNION

SELECT IFNULL(c.class, o.ship) AS class_or_ship
FROM lab2.Outcomes o
LEFT JOIN lab2.Classes c ON o.ship = c.class
WHERE NOT EXISTS (
    SELECT * FROM lab2.Ships s WHERE s.name = o.ship
)
GROUP BY o.ship
HAVING COUNT(o.ship) = 1;

-- lab1 1
-- Видає повне ім'я та email  бронювання
SELECT full_name, email
FROM lab1.client
WHERE id IN (
    SELECT client_id
    FROM lab1.booking
);

-- lab1 2
-- Видає готелі з найбільшим рейтингом
SELECT name, stars
FROM lab1.Hotel
WHERE stars = (SELECT MAX(stars) FROM lab1.Hotel);

-- lab1 3
-- Видає НАЙДЕШЕВШИЙ готель з ДОСТУПНИМ бронюванням
SELECT h.name, r.price_per_night
FROM lab1.room r
JOIN lab1.Hotel h ON r.Hotel_id = h.id
WHERE r.price_per_night = (SELECT MIN(price_per_night) FROM lab1.room WHERE available = 1);

-- lab1 4
-- Видає всіх клієнтів, що оплатили номер карткою Mastercard
SELECT c.full_name, p.payment_amount
FROM lab1.client c
JOIN lab1.payment p ON c.id = p.client_id
WHERE p.card_number LIKE '5___%';

-- lab1 5
-- Видає готелі з кількістю додаткових послуг більшою за середню
SELECT h.id, h.name, COUNT(ha.amenities_id) AS amenities_count
FROM lab1.Hotel h
JOIN lab1.Hotel_has_amenities ha ON h.id = ha.Hotel_id
GROUP BY h.id, h.name
HAVING COUNT(ha.amenities_id) > (
    SELECT AVG(amenities_count)
    FROM (
        SELECT COUNT(ha2.amenities_id) AS amenities_count
        FROM lab1.Hotel_has_amenities ha2
        GROUP BY ha2.Hotel_id
    ) AS avg_amenities
);

START TRANSACTION;
USE lab1;
INSERT INTO lab1.Hotel_has_amenities (`Hotel_id`, `Hotel_location_id`, `amenities_id`) VALUES (2, 2, 5);
COMMIT;

SELECT h.id, h.name, COUNT(ha.amenities_id) AS amenities_count
FROM lab1.Hotel h
JOIN lab1.Hotel_has_amenities ha ON h.id = ha.Hotel_id
GROUP BY h.id, h.name
HAVING COUNT(ha.amenities_id) > (
    SELECT AVG(amenities_count)
    FROM (
        SELECT COUNT(ha2.amenities_id) AS amenities_count
        FROM lab1.Hotel_has_amenities ha2
        GROUP BY ha2.Hotel_id
    ) AS avg_amenities
);

START TRANSACTION;
USE lab1;
DELETE FROM lab1.Hotel_has_amenities
WHERE (`Hotel_id`, `Hotel_location_id`, `amenities_id`) = (2, 2, 5);
COMMIT;



Select c.full_name, b.check_in_date
From lab1.client c
Join booking b on b.client_id = c.id
Join room r on b.room_id = r.id
Where r.room_type = 'Double';



SELECT * FROM lab3.room;



-- Select h.name, l.city, l.country, h.stars
-- From lab3.Hotel h
-- Join lab3.Location l on h.location_id = l.id
-- Where h.stars = 4;


-- Select h.name, r.price_per_night
-- From lab3.Hotel h
-- Join lab3.Room r on h.id = r.hotel_id
-- Where r.price_per_night < 100;


-- Select c.full_name, b.check_in_date, b.check_out_date 
-- From lab3.booking b
-- Join lab3.client c on c.id = b.client_id;


-- Select h.name, a.name 
-- From lab3.Hotel h
-- JOIN lab3.hotel_has_amenities ha ON h.id = ha.hotel_id
-- JOIN lab3.amenities a ON ha.amenities_id = a.id
-- Where a.name = "Wi-Fi" or a.name = "Spa"
-- Order by h.name;


-- Select h.name, r.rating, r.comment, c.full_name
-- From lab3.client c
-- Join lab3.review r on r.client_id = c.id
-- Join lab3.hotel h on h.id = r.hotel_id
-- Where h.name = 'ibis Styles Lviv Center'
-- Order by h.name;


-- Select c.full_name, h.name, ch.name
-- From lab3.Client c
-- Join lab3.booking b on b.client_id = c.id
-- Join lab3.room r on r.id = b.room_id
-- Join lab3.hotel h on h.id = r.hotel_id
-- Join lab3.chain ch on ch.id = h.chain_id
-- Where ch.id = 1 OR ch.id = 3;

-- Select h.name, r.room_type, AVG(r.price_per_night)
-- From lab3.hotel h
-- Join lab3.room r on h.id = r.hotel_id
-- Group by h.id, r.room_type;



-- Select h.name, AVG(r.rating) 
-- From lab3.hotel h
-- Join lab3.review r on h.id = r.hotel_id
-- Group by  h.name, r.rating;


-- Select h.name, COUNT(a.hotel_id)
-- From lab3.hotel h
-- Join lab3.hotel_has_amenities a on h.id = a.hotel_id
-- Group by h.name, a.hotel_id;


-- Use lab1;
-- Select c.full_name, c.email, dc.name, dc.discound, b.id
-- From client c
-- Join discount_cards dc on c.discount_cards_id = dc.id
-- Join booking b on c.id = b.client_id
-- Where c.discount_cards_id is not null


-- Select h.name, AVG(r.price_per_night) as average_price
-- From Hotel h
-- Join room r on h.id = r.hotel_id
-- Group by h.name
-- Having average_price > (Select AVG(price_per_night) From room)


















