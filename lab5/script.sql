DROP DATABASE IF EXISTS lab5;
CREATE DATABASE lab5;
USE lab5;

-- Drop existing tables if they exist
SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS review;
DROP TABLE IF EXISTS booking;
DROP TABLE IF EXISTS payment;
DROP TABLE IF EXISTS client;
DROP TABLE IF EXISTS room;
DROP TABLE IF EXISTS hotel_has_amenities;
DROP TABLE IF EXISTS amenities;
DROP TABLE IF EXISTS hotel;
DROP TABLE IF EXISTS chain;
DROP TABLE IF EXISTS location;
DROP TABLE IF EXISTS discount_cards;
DROP TABLE IF EXISTS booking_log;
DROP TABLE IF EXISTS client_hotel;
DROP TABLE IF EXISTS loyalty_program;

SET FOREIGN_KEY_CHECKS = 1;

-- Create location table
CREATE TABLE IF NOT EXISTS location (
  location_id INT NOT NULL AUTO_INCREMENT,
  city VARCHAR(45) NOT NULL,
  country VARCHAR(45) NOT NULL,
  PRIMARY KEY (location_id)
) ENGINE = InnoDB;

-- Create chain table
CREATE TABLE IF NOT EXISTS chain (
  chain_id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(45) NOT NULL,
  PRIMARY KEY (chain_id)
) ENGINE = InnoDB;

-- Create hotel table
CREATE TABLE IF NOT EXISTS hotel (
  hotel_id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(45) NOT NULL,
  address VARCHAR(100) NOT NULL,
  room_num INT,
  location_id INT NOT NULL,
  stars INT NOT NULL,
  chain_id INT,
  PRIMARY KEY (hotel_id),
  FOREIGN KEY (location_id) REFERENCES location(location_id) ON DELETE CASCADE,
  FOREIGN KEY (chain_id) REFERENCES chain(chain_id) ON DELETE SET NULL
) ENGINE = InnoDB;

-- Create room table
CREATE TABLE IF NOT EXISTS room (
  room_id INT NOT NULL AUTO_INCREMENT,
  room_type VARCHAR(45) NOT NULL,
  price_per_night DECIMAL(10, 2) NOT NULL,
  available TINYINT NOT NULL,
  hotel_id INT NOT NULL,
  PRIMARY KEY (room_id),
  FOREIGN KEY (hotel_id) REFERENCES hotel(hotel_id) ON DELETE CASCADE
) ENGINE = InnoDB;

-- Create discount_cards table
CREATE TABLE IF NOT EXISTS discount_cards (
  discount_cards_id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(45) NOT NULL,
  discount VARCHAR(10) NOT NULL,
  PRIMARY KEY (discount_cards_id)
) ENGINE = InnoDB;

-- Create loyalty_program table
CREATE TABLE IF NOT EXISTS loyalty_program (
  loyalty_program_id INT NOT NULL AUTO_INCREMENT,
  program_name VARCHAR(100) NOT NULL,
  tier_level VARCHAR(20),
  discount_percent DECIMAL(5,2) DEFAULT 0.00,
  PRIMARY KEY (loyalty_program_id),
  UNIQUE KEY uq_loyalty_program_name (program_name)
) ENGINE = InnoDB;

-- Create client table
CREATE TABLE IF NOT EXISTS client (
  client_id INT NOT NULL AUTO_INCREMENT,
  full_name VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL,
  phone_num VARCHAR(20) NOT NULL,
  discount_cards_id INT,
  loyalty_program_id INT,
  PRIMARY KEY (client_id),
  FOREIGN KEY (discount_cards_id) REFERENCES discount_cards(discount_cards_id) ON DELETE SET NULL,
  FOREIGN KEY (loyalty_program_id) REFERENCES loyalty_program(loyalty_program_id) ON DELETE SET NULL
) ENGINE = InnoDB;

-- Create payment table
CREATE TABLE IF NOT EXISTS payment (
  payment_id INT NOT NULL AUTO_INCREMENT,
  card_number VARCHAR(20),
  payment_amount DECIMAL(10, 2) NOT NULL,
  payment_date DATE NOT NULL,
  status TINYINT NOT NULL,
  client_id INT NOT NULL,
  PRIMARY KEY (payment_id),
  FOREIGN KEY (client_id) REFERENCES client(client_id) ON DELETE CASCADE
) ENGINE = InnoDB;

-- Create review table
CREATE TABLE IF NOT EXISTS review (
  review_id INT NOT NULL AUTO_INCREMENT,
  rating INT NOT NULL,
  comment TEXT,
  client_id INT NOT NULL,
  hotel_id INT NOT NULL,
  PRIMARY KEY (review_id),
  FOREIGN KEY (client_id) REFERENCES client(client_id) ON DELETE CASCADE,
  FOREIGN KEY (hotel_id) REFERENCES hotel(hotel_id) ON DELETE CASCADE
) ENGINE = InnoDB;

-- Create amenities table
CREATE TABLE IF NOT EXISTS amenities (
  amenities_id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(45) NOT NULL,
  PRIMARY KEY (amenities_id)
) ENGINE = InnoDB;

-- Create hotel_has_amenities table
CREATE TABLE IF NOT EXISTS hotel_has_amenities (
  hotel_id INT NOT NULL,
  amenities_id INT NOT NULL,
  PRIMARY KEY (hotel_id, amenities_id),
  FOREIGN KEY (hotel_id) REFERENCES hotel(hotel_id) ON DELETE CASCADE,
  FOREIGN KEY (amenities_id) REFERENCES amenities(amenities_id) ON DELETE CASCADE
) ENGINE = InnoDB;

-- Create booking table
CREATE TABLE IF NOT EXISTS booking (
  booking_id INT NOT NULL AUTO_INCREMENT,
  check_in_date DATE NOT NULL,
  check_out_date DATE NOT NULL,
  total_price DECIMAL(10, 2) NOT NULL,
  room_id INT NOT NULL,
  client_id INT NOT NULL,
  payment_id INT,
  PRIMARY KEY (booking_id),
  FOREIGN KEY (room_id) REFERENCES room(room_id) ON DELETE CASCADE,
  FOREIGN KEY (client_id) REFERENCES client(client_id) ON DELETE CASCADE,
  FOREIGN KEY (payment_id) REFERENCES payment(payment_id) ON DELETE SET NULL
) ENGINE = InnoDB;

-- Insert data for location
INSERT IGNORE INTO location (city, country) VALUES
('Lviv', 'Ukraine'),
('Kyiv', 'Ukraine'),
('Warsaw', 'Poland'),
('Berlin', 'Germany'),
('Vienna', 'Austria'),
('Paris', 'France'),
('Madrid', 'Spain'),
('Rome', 'Italy'),
('London', 'UK'),
('Tokyo', 'Japan');

-- Insert data for chain
INSERT IGNORE INTO chain (name) VALUES
('Ibis'), ('Mercure'), ('Novotel'), ('Hilton'), ('Holiday Inn');

-- Insert data for hotel
INSERT INTO hotel (name, address, room_num, location_id, stars, chain_id) VALUES
('ibis Styles Lviv Center', 'Shukhevycha Street, 3', 77, 1, 3, 1),
('Mercure Kyiv Congress', 'Vadima Hetmana Street, 6', 160, 2, 4, 2),
('Novotel Warszawa Airport', 'UL. 1 Sierpnia 1', 281, 3, 4, 3),
('ibis Wels', 'Maria Theresia Strasse 44', 116, 5, 3, 1),
('Hotel Mercure Vienne City', 'Bayerhamerstrasse 14 a', 121, 4, 4, 2),
('Hilton Paris Opera', 'Rue Saint-Lazare, 108', 268, 6, 5, 4),
('Holiday Inn Madrid', 'Calle Alcala 476', 170, 7, 4, 5),
('Novotel Rome Eur', 'Viale Oceano Pacifico 153', 215, 8, 4, 3),
('Hilton London Kensington', 'Holland Park Ave', 235, 9, 5, 4),
('ibis Tokyo Shinjuku', '7-10-5 Nishi-Shinjuku', 206, 10, 3, 1);

-- Insert data for room
INSERT IGNORE INTO room (room_type, price_per_night, available, hotel_id) VALUES
('Single', 50, 1, 1),
('Double', 80, 1, 1),
('Suite', 150, 1, 2),
('Deluxe', 200, 1, 3),
('Single', 55, 1, 4),
('Deluxe', 220, 1, 5),
('Double', 90, 1, 6),
('Single', 60, 1, 7),
('Suite', 175, 1, 8),
('Single', 65, 1, 9);

-- Insert data for discount_cards
INSERT IGNORE INTO discount_cards (name, discount) VALUES
('silver', '5%'),
('gold', '10%'),
('platinum', '15%'),
('diamond', '20%');

-- Seed: loyalty_program
INSERT IGNORE INTO loyalty_program (program_name, tier_level, discount_percent) VALUES
('Basic',   'Bronze',   0.00),
('Silver',  'Silver',   5.00),
('Gold',    'Gold',    10.00),
('Platinum','Platinum', 15.00);

-- Insert data for client
INSERT IGNORE INTO client (full_name, email, phone_num, discount_cards_id, loyalty_program_id) VALUES
('John Doe', 'johndoe@gmail.com', '+380123456789', 1, 3),
('Jane Smith', 'janesmith@gmail.com', '+380987654321', 2, 2),
('Mark Brown', 'markbrown@gmail.com', '+48123456789', NULL, NULL),
('Anna Johnson', 'annajonson@gmail.com', '+49301234567', 3, 2),
('Tom Lee', 'tomlee@gmail.com', '+43123456789', NULL, 4),
('Emily White', 'emilywhite@gmail.com', '+441234567890', 1, NULL),
('Michael Green', 'michaelgreen@gmail.com', '+34123456789', 2, NULL),
('Luca Rossi', 'lucarossi@gmail.com', '+390123456789', 3, NULL),
('Hiroshi Tanaka', 'hiroshitanaka@gmail.com', '+811234567890', NULL, 1),
('Olivia Miller', 'oliviamiller@gmail.com', '+49123456789', 4, NULL);

-- Insert data for payment
INSERT IGNORE INTO payment (card_number, payment_amount, payment_date, status, client_id) VALUES
('5234567890123456', 250, '2024-09-10', 1, 1),
('545678901234567', 400, '2024-09-11', 1, 2),
('4456789012345678', 600, '2024-09-12', 0, 3),
('4567890123456789', 1000, '2024-09-13', 1, 4),
('5678901234567890', 275, '2024-09-14', 1, 5),
('5789012345678901', 450, '2024-09-15', 1, 6),
('5890123456789012', 500, '2024-09-16', 1, 7),
('5901234567890123', 550, '2024-09-17', 0, 8),
('4012345678901234', 320, '2024-09-18', 1, 9),
('4123456789012345', 600, '2024-09-19', 1, 10);

-- Insert data for booking
INSERT IGNORE INTO booking (check_in_date, check_out_date, total_price, room_id, client_id, payment_id) VALUES
('2024-09-10', '2024-09-15', 250, 1, 1, 1),
('2024-09-11', '2024-09-16', 400, 2, 2, 2),
('2024-09-12', '2024-09-17', 600, 3, 3, 3),
('2024-09-13', '2024-09-18', 1000, 4, 4, 4),
('2024-09-13', '2024-09-19', 275, 5, 5, 5),
('2024-09-14', '2024-09-20', 450, 6, 6, 6),
('2024-09-15', '2024-09-21', 500, 7, 7, 7),
('2024-09-16', '2024-09-22', 550, 8, 8, 8),
('2024-09-17', '2024-09-23', 320, 9, 9, 9),
('2024-09-18', '2024-09-24', 600, 10, 10, 10);

-- Insert data for review
INSERT IGNORE INTO review (rating, comment, client_id, hotel_id) VALUES
(4, 'Had a pleasant stay.', 10, 1),
(5, 'Excellent location and staff.', 1, 2),
(3, 'Could be cleaner.', 2, 3),
(4, 'Good amenities and comfortable beds.', 3, 1),
(5, 'Loved the breakfast!', 4, 4),
(3, 'Noise from the street was disturbing.', 5, 5),
(4, 'Friendly staff and good service.', 6, 6),
(2, 'Room was small and cramped.', 7, 7),
(4, 'Nice place, enjoyed the stay.', 8, 8),
(5, 'Amazing experience, highly recommend!', 9, 9),
(3, 'Decent for the price.', 10, 10),
(4, 'Very clean and organized.', 1, 1);

-- Insert data for amenities
INSERT IGNORE INTO amenities (name) VALUES
('Wi-Fi'), ('Swimming Pool'), ('Gym'), ('Spa'), ('Parking'), 
('Restaurant'), ('Bar'), ('Room Service'), ('Conference Room'), ('Laundry Service');

-- Insert data for hotel_has_amenities
INSERT IGNORE INTO hotel_has_amenities (hotel_id, amenities_id) VALUES
(1, 1), (1, 2), (1, 3), 
(2, 1), (2, 4), 
(3, 1), (3, 5), 
(4, 6), 
(5, 1), (5, 3),
(6, 2), (6, 7), 
(7, 5), (7, 6),
(8, 3), (8, 8),
(9, 9), (9, 10),
(10, 1), (10, 4);
