-- SHOW TABLES;

-- DESCRIBE amenities;
-- DESCRIBE booking;
-- DESCRIBE booking_log;
-- DESCRIBE chain;
-- DESCRIBE client;
-- DESCRIBE client_hotel;
-- DESCRIBE discount_cards;
-- DESCRIBE hotel;
-- DESCRIBE hotel_has_amenities;
-- DESCRIBE location;
-- DESCRIBE loyalty_program;
-- DESCRIBE payment;
-- DESCRIBE review;
-- DESCRIBE room;


-- INSERT INTO loyalty_program (program_name, description)
-- VALUES ('Gold Membership', 'Special discounts for loyal customers');
-- SELECT * FROM loyalty_program;


-- CALL insert_client('Alice Brown', 'alice@example.com', '987654321', NULL);
-- SELECT * FROM client WHERE full_name = 'Alice Brown';


-- UPDATE location SET city = 'Updated City' WHERE location_id = 1;


-- CALL insert_client('Bob Smith', 'bob@example.com', '5555555', NULL);
-- INSERT INTO hotel (name, address, stars, location_id) VALUES ('Hotel Grand', '123 Main St', 5, 1);

-- CALL insert_client_hotel_relation('Bob Smith', 'Hotel Grand');
-- SELECT * FROM client_hotel;

-- SELECT * FROM amenities;
-- CALL insert_bulk_amenities();
-- SELECT * FROM amenities;


-- CALL calculate_stat('client', 'client_id', 'MAX');


-- INSERT INTO booking (booking_id ,check_in_date, check_out_date, total_price, room_id, client_id)
-- VALUES (11, CURDATE(), DATE_ADD(CURDATE(), INTERVAL 3 DAY), 500, 1, 1);
-- SELECT * FROM booking;

-- DELETE FROM booking WHERE booking_id = 11;
-- SELECT * FROM booking_log;


