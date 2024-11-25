USE lab5;

DROP PROCEDURE IF EXISTS insert_client;
DROP PROCEDURE IF EXISTS calculate_stat;
DROP PROCEDURE IF EXISTS insert_bulk_amenities;
DROP PROCEDURE IF EXISTS distribute_data_randomly;
DROP PROCEDURE IF EXISTS insert_client_hotel_relation;

-- 1. Додаткова таблиця loyalty_program та тригер для зв'язку 1:M з client без фізичного зовнішнього ключа
CREATE TABLE IF NOT EXISTS loyalty_program (
    id INT AUTO_INCREMENT PRIMARY KEY,
    program_name VARCHAR(100) NOT NULL,
    description TEXT
);

-- Наповнення таблиці loyalty_program тестовими даними
INSERT INTO loyalty_program (program_name, description)
VALUES 
('Gold Membership', 'Premium benefits for loyal clients'),
('Silver Membership', 'Standard benefits for clients');

ALTER TABLE client
ADD COLUMN loyalty_program_id INT;

-- DELIMITER //

-- CREATE TRIGGER client_loyalty_program_check
-- BEFORE INSERT ON client
-- FOR EACH ROW
-- BEGIN
--     DECLARE loyalty_exists INT;

--     -- Перевірка, чи задано loyalty_program_id
--     IF NEW.loyalty_program_id IS NOT NULL THEN
--         SELECT COUNT(*) INTO loyalty_exists
--         FROM loyalty_program
--         WHERE id = NEW.loyalty_program_id;

--         -- Якщо програма не існує, встановлюємо NULL
--         IF loyalty_exists = 0 THEN
--             SET NEW.loyalty_program_id = NULL;
--         END IF;
--     END IF;
-- END;
-- //

-- DELIMITER ;

DELIMITER //

CREATE TRIGGER client_loyalty_program_check
BEFORE INSERT ON client
FOR EACH ROW
BEGIN
    DECLARE loyalty_exists INT;

    -- Перевірка, чи задано loyalty_program_id
    IF NEW.loyalty_program_id IS NOT NULL THEN
        SELECT COUNT(*) INTO loyalty_exists
        FROM loyalty_program
        WHERE id = NEW.loyalty_program_id;

        -- Якщо програма не існує, сигналізуємо про помилку
        IF loyalty_exists = 0 THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Loyalty program not found';
        END IF;
    END IF;

    -- Додатково можна встановити обмеження (як у прикладі друга):
    IF NEW.full_name IS NULL OR NEW.email IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Full name and email are required';
    END IF;
END;
//

DELIMITER ;

-- 2. Параметризована процедура вставки клієнта у таблицю client
-- DELIMITER //

-- CREATE PROCEDURE insert_client(
--     IN full_name VARCHAR(100),
--     IN email VARCHAR(100),
--     IN phone_num VARCHAR(20),
--     IN discount_cards_id INT,
--     IN loyalty_program_id INT
-- )
-- BEGIN
--     -- Оголошення змінних має бути на початку блоку BEGIN
--     DECLARE loyalty_exists INT;

--     -- Перевірка існування програми лояльності
--     IF loyalty_program_id IS NOT NULL THEN
--         SELECT COUNT(*) INTO loyalty_exists
--         FROM loyalty_program
--         WHERE id = loyalty_program_id;

--         IF loyalty_exists = 0 THEN
--             SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Loyalty program not found';
--         END IF;
--     END IF;

--     -- Вставка запису в таблицю client
--     INSERT INTO client (full_name, email, phone_num, discount_cards_id, loyalty_program_id)
--     VALUES (full_name, email, phone_num, discount_cards_id, loyalty_program_id);
-- END;
-- //

-- DELIMITER ;

DELIMITER //

CREATE PROCEDURE insert_client(
    IN full_name VARCHAR(100),
    IN email VARCHAR(100),
    IN phone_num VARCHAR(20),
    IN discount_cards_id INT,
    IN loyalty_program_id INT
)
BEGIN
    -- Проста вставка запису в таблицю client
    INSERT INTO client (full_name, email, phone_num, discount_cards_id, loyalty_program_id)
    VALUES (full_name, email, phone_num, discount_cards_id, loyalty_program_id);
END;
//

DELIMITER ;


-- 3. Процедура для вставки зв'язку M:M між client і hotel (через client_hotel)
CREATE TABLE IF NOT EXISTS client_hotel (
    client_id INT,
    hotel_id INT,
    PRIMARY KEY (client_id, hotel_id),
    FOREIGN KEY (client_id) REFERENCES client(client_id) ON DELETE CASCADE,
    FOREIGN KEY (hotel_id) REFERENCES hotel(hotel_id) ON DELETE CASCADE
);

DELIMITER //

CREATE PROCEDURE insert_client_hotel_relation(
    IN client_name VARCHAR(100),
    IN hotel_name VARCHAR(45)
)
BEGIN
    DECLARE clientID INT DEFAULT NULL;
    DECLARE hotelID INT DEFAULT NULL;

    -- Отримуємо ID клієнта
    SELECT client_id INTO clientID FROM client WHERE full_name = client_name LIMIT 1;

    -- Отримуємо ID готелю
    SELECT hotel_id INTO hotelID FROM hotel WHERE name = hotel_name LIMIT 1;

    -- Перевірка існування клієнта
    IF clientID IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Client not found';
    END IF;

    -- Перевірка існування готелю
    IF hotelID IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Hotel not found';
    END IF;

    -- Вставка запису, якщо обидва ID знайдено
    INSERT INTO client_hotel (client_id, hotel_id) VALUES (clientID, hotelID);
END;
//

DELIMITER ;

-- 4. Пакетна вставка 10 записів у таблицю amenities
DELIMITER //
CREATE PROCEDURE insert_bulk_amenities()
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= 10 DO
        INSERT INTO amenities (name) VALUES (CONCAT('Noname', i));
        SET i = i + 1;
    END WHILE;
END;
//
DELIMITER ;

-- 5. Користувацька функція для обчислення MAX, MIN, SUM або AVG для довільного стовпця
DELIMITER //

CREATE PROCEDURE calculate_stat(
    IN table_name VARCHAR(50),
    IN column_name VARCHAR(50),
    IN operation VARCHAR(10)
)
BEGIN
    -- Construct the dynamic SQL query
    SET @query = CONCAT('SELECT ', operation, '(', column_name, ') AS result FROM ', table_name);

    -- Debugging: Log the generated query (remove in production)
    -- SELECT @query AS debug_query;

    -- Execute the dynamic SQL and return the result directly
    PREPARE stmt FROM @query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END;
//

DELIMITER ;

-- 6. Процедура з курсором для створення двох таблиць з випадковим розподілом даних
DELIMITER //
CREATE PROCEDURE distribute_data_randomly()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE temp_client_id INT;
    DECLARE cursor1 CURSOR FOR SELECT client_id FROM client; -- Заміна id на client_id
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    SET @table1 = CONCAT('client_data_', UNIX_TIMESTAMP(), '_1');
    SET @table2 = CONCAT('client_data_', UNIX_TIMESTAMP(), '_2');

    -- Створення нових таблиць
    SET @create_query1 = CONCAT('CREATE TABLE ', @table1, ' LIKE client');
    SET @create_query2 = CONCAT('CREATE TABLE ', @table2, ' LIKE client');
    PREPARE stmt1 FROM @create_query1;
    EXECUTE stmt1;
    DEALLOCATE PREPARE stmt1;
    PREPARE stmt2 FROM @create_query2;
    EXECUTE stmt2;
    DEALLOCATE PREPARE stmt2;

    -- Відкриття курсора
    OPEN cursor1;

    read_loop: LOOP
        FETCH cursor1 INTO temp_client_id;
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Випадковий розподіл клієнтів
        IF RAND() > 0.5 THEN
            SET @insert_query = CONCAT('INSERT INTO ', @table1, ' SELECT * FROM client WHERE client_id = ', temp_client_id);
        ELSE
            SET @insert_query = CONCAT('INSERT INTO ', @table2, ' SELECT * FROM client WHERE client_id = ', temp_client_id);
        END IF;

        PREPARE stmt FROM @insert_query;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
    END LOOP;

    -- Закриття курсора
    CLOSE cursor1;
END;
//
DELIMITER ;

-- 7. Тригер для заборони модифікації таблиці location
DELIMITER //
CREATE TRIGGER prevent_location_update
BEFORE UPDATE ON location
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Updates are not allowed on the location table';
END;
//
DELIMITER ;

-- 8. Логування видалення даних з таблиці booking
CREATE TABLE IF NOT EXISTS booking_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id INT,
    deleted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DELIMITER //
CREATE TRIGGER log_booking_delete
AFTER DELETE ON booking
FOR EACH ROW
BEGIN
    INSERT INTO booking_log (booking_id) VALUES (OLD.booking_id);
END;
//
DELIMITER ;

-- 9. Тригер для забезпечення мінімальної кардинальності у 6 записів у таблиці review
DELIMITER //
CREATE TRIGGER maintain_min_clients
BEFORE DELETE ON client
FOR EACH ROW
BEGIN
    DECLARE client_count INT;
    SELECT COUNT(*) INTO client_count FROM client;
    IF client_count <= 8 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Minimum 8 clients are required';
    END IF;
END;
//
DELIMITER ;
