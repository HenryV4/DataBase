/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19  Distrib 10.11.14-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: 127.0.0.1    Database: lab5
-- ------------------------------------------------------
-- Server version	10.11.14-MariaDB-0+deb12u2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `amenities`
--

DROP TABLE IF EXISTS `amenities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `amenities` (
  `amenities_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`amenities_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amenities`
--

LOCK TABLES `amenities` WRITE;
/*!40000 ALTER TABLE `amenities` DISABLE KEYS */;
INSERT INTO `amenities` VALUES
(1,'Wi-Fi'),
(2,'Swimming Pool'),
(3,'Gym'),
(4,'Spa'),
(5,'Parking'),
(6,'Restaurant'),
(7,'Bar'),
(8,'Room Service'),
(9,'Conference Room'),
(10,'Laundry Service');
/*!40000 ALTER TABLE `amenities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `booking`
--

DROP TABLE IF EXISTS `booking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `booking` (
  `booking_id` int(11) NOT NULL AUTO_INCREMENT,
  `check_in_date` date NOT NULL,
  `check_out_date` date NOT NULL,
  `total_price` decimal(10,2) NOT NULL,
  `room_id` int(11) NOT NULL,
  `client_id` int(11) NOT NULL,
  `payment_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`booking_id`),
  KEY `room_id` (`room_id`),
  KEY `client_id` (`client_id`),
  KEY `payment_id` (`payment_id`),
  CONSTRAINT `booking_ibfk_1` FOREIGN KEY (`room_id`) REFERENCES `room` (`room_id`) ON DELETE CASCADE,
  CONSTRAINT `booking_ibfk_2` FOREIGN KEY (`client_id`) REFERENCES `client` (`client_id`) ON DELETE CASCADE,
  CONSTRAINT `booking_ibfk_3` FOREIGN KEY (`payment_id`) REFERENCES `payment` (`payment_id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booking`
--

LOCK TABLES `booking` WRITE;
/*!40000 ALTER TABLE `booking` DISABLE KEYS */;
INSERT INTO `booking` VALUES
(1,'2024-09-10','2024-09-15',250.00,1,1,1),
(2,'2024-09-11','2024-09-16',400.00,2,2,2),
(3,'2024-09-12','2024-09-17',600.00,3,3,3),
(4,'2024-09-13','2024-09-18',1000.00,4,4,4),
(5,'2024-09-13','2024-09-19',275.00,5,5,5),
(6,'2024-09-14','2024-09-20',450.00,6,6,6),
(7,'2024-09-15','2024-09-21',500.00,7,7,7),
(8,'2024-09-16','2024-09-22',550.00,8,8,8),
(9,'2024-09-17','2024-09-23',320.00,9,9,9),
(10,'2024-09-18','2024-09-24',600.00,10,10,10);
/*!40000 ALTER TABLE `booking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chain`
--

DROP TABLE IF EXISTS `chain`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `chain` (
  `chain_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`chain_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chain`
--

LOCK TABLES `chain` WRITE;
/*!40000 ALTER TABLE `chain` DISABLE KEYS */;
INSERT INTO `chain` VALUES
(1,'Ibis'),
(2,'Mercure'),
(3,'Novotel'),
(4,'Hilton'),
(5,'Holiday Inn');
/*!40000 ALTER TABLE `chain` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `client`
--

DROP TABLE IF EXISTS `client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `client` (
  `client_id` int(11) NOT NULL AUTO_INCREMENT,
  `full_name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone_num` varchar(20) NOT NULL,
  `discount_cards_id` int(11) DEFAULT NULL,
  `loyalty_program_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`client_id`),
  KEY `discount_cards_id` (`discount_cards_id`),
  KEY `loyalty_program_id` (`loyalty_program_id`),
  CONSTRAINT `client_ibfk_1` FOREIGN KEY (`discount_cards_id`) REFERENCES `discount_cards` (`discount_cards_id`) ON DELETE SET NULL,
  CONSTRAINT `client_ibfk_2` FOREIGN KEY (`loyalty_program_id`) REFERENCES `loyalty_program` (`loyalty_program_id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client`
--

LOCK TABLES `client` WRITE;
/*!40000 ALTER TABLE `client` DISABLE KEYS */;
INSERT INTO `client` VALUES
(1,'John Doe','johndoe@gmail.com','+380123456789',1,3),
(2,'Jane Smith','janesmith@gmail.com','+380987654321',2,2),
(3,'Mark Brown','markbrown@gmail.com','+48123456789',NULL,NULL),
(4,'Anna Johnson','annajonson@gmail.com','+49301234567',3,2),
(5,'Tom Lee','tomlee@gmail.com','+43123456789',NULL,4),
(6,'Emily White','emilywhite@gmail.com','+441234567890',1,NULL),
(7,'Michael Green','michaelgreen@gmail.com','+34123456789',2,NULL),
(8,'Luca Rossi','lucarossi@gmail.com','+390123456789',3,NULL),
(9,'Hiroshi Tanaka','hiroshitanaka@gmail.com','+811234567890',NULL,1),
(10,'Olivia Miller','oliviamiller@gmail.com','+49123456789',4,NULL);
/*!40000 ALTER TABLE `client` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `discount_cards`
--

DROP TABLE IF EXISTS `discount_cards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `discount_cards` (
  `discount_cards_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `discount` varchar(10) NOT NULL,
  PRIMARY KEY (`discount_cards_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discount_cards`
--

LOCK TABLES `discount_cards` WRITE;
/*!40000 ALTER TABLE `discount_cards` DISABLE KEYS */;
INSERT INTO `discount_cards` VALUES
(1,'silver','5%'),
(2,'gold','10%'),
(3,'platinum','15%'),
(4,'diamond','20%');
/*!40000 ALTER TABLE `discount_cards` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hotel`
--

DROP TABLE IF EXISTS `hotel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `hotel` (
  `hotel_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `address` varchar(100) NOT NULL,
  `room_num` int(11) DEFAULT NULL,
  `location_id` int(11) NOT NULL,
  `stars` int(11) NOT NULL,
  `chain_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`hotel_id`),
  KEY `location_id` (`location_id`),
  KEY `chain_id` (`chain_id`),
  CONSTRAINT `hotel_ibfk_1` FOREIGN KEY (`location_id`) REFERENCES `location` (`location_id`) ON DELETE CASCADE,
  CONSTRAINT `hotel_ibfk_2` FOREIGN KEY (`chain_id`) REFERENCES `chain` (`chain_id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hotel`
--

LOCK TABLES `hotel` WRITE;
/*!40000 ALTER TABLE `hotel` DISABLE KEYS */;
INSERT INTO `hotel` VALUES
(1,'ibis Styles Lviv Center','Shukhevycha Street, 3',77,1,3,1),
(2,'Mercure Kyiv Congress','Vadima Hetmana Street, 6',160,2,4,2),
(3,'Novotel Warszawa Airport','UL. 1 Sierpnia 1',281,3,4,3),
(4,'ibis Wels','Maria Theresia Strasse 44',116,5,3,1),
(5,'Hotel Mercure Vienne City','Bayerhamerstrasse 14 a',121,4,4,2),
(6,'Hilton Paris Opera','Rue Saint-Lazare, 108',268,6,5,4),
(7,'Holiday Inn Madrid','Calle Alcala 476',170,7,4,5),
(8,'Novotel Rome Eur','Viale Oceano Pacifico 153',215,8,4,3),
(9,'Hilton London Kensington','Holland Park Ave',235,9,5,4),
(10,'ibis Tokyo Shinjuku','7-10-5 Nishi-Shinjuku',206,10,3,1);
/*!40000 ALTER TABLE `hotel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hotel_has_amenities`
--

DROP TABLE IF EXISTS `hotel_has_amenities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `hotel_has_amenities` (
  `hotel_id` int(11) NOT NULL,
  `amenities_id` int(11) NOT NULL,
  PRIMARY KEY (`hotel_id`,`amenities_id`),
  KEY `amenities_id` (`amenities_id`),
  CONSTRAINT `hotel_has_amenities_ibfk_1` FOREIGN KEY (`hotel_id`) REFERENCES `hotel` (`hotel_id`) ON DELETE CASCADE,
  CONSTRAINT `hotel_has_amenities_ibfk_2` FOREIGN KEY (`amenities_id`) REFERENCES `amenities` (`amenities_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hotel_has_amenities`
--

LOCK TABLES `hotel_has_amenities` WRITE;
/*!40000 ALTER TABLE `hotel_has_amenities` DISABLE KEYS */;
INSERT INTO `hotel_has_amenities` VALUES
(1,1),
(1,2),
(1,3),
(2,1),
(2,4),
(3,1),
(3,5),
(4,6),
(5,1),
(5,3),
(6,2),
(6,7),
(7,5),
(7,6),
(8,3),
(8,8),
(9,9),
(9,10),
(10,1),
(10,4);
/*!40000 ALTER TABLE `hotel_has_amenities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `location`
--

DROP TABLE IF EXISTS `location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `location` (
  `location_id` int(11) NOT NULL AUTO_INCREMENT,
  `city` varchar(45) NOT NULL,
  `country` varchar(45) NOT NULL,
  PRIMARY KEY (`location_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `location`
--

LOCK TABLES `location` WRITE;
/*!40000 ALTER TABLE `location` DISABLE KEYS */;
INSERT INTO `location` VALUES
(1,'Lviv','Ukraine'),
(2,'Kyiv','Ukraine'),
(3,'Warsaw','Poland'),
(4,'Berlin','Germany'),
(5,'Vienna','Austria'),
(6,'Paris','France'),
(7,'Madrid','Spain'),
(8,'Rome','Italy'),
(9,'London','UK'),
(10,'Tokyo','Japan');
/*!40000 ALTER TABLE `location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loyalty_program`
--

DROP TABLE IF EXISTS `loyalty_program`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `loyalty_program` (
  `loyalty_program_id` int(11) NOT NULL AUTO_INCREMENT,
  `program_name` varchar(100) NOT NULL,
  `tier_level` varchar(20) DEFAULT NULL,
  `discount_percent` decimal(5,2) DEFAULT 0.00,
  PRIMARY KEY (`loyalty_program_id`),
  UNIQUE KEY `uq_loyalty_program_name` (`program_name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loyalty_program`
--

LOCK TABLES `loyalty_program` WRITE;
/*!40000 ALTER TABLE `loyalty_program` DISABLE KEYS */;
INSERT INTO `loyalty_program` VALUES
(1,'Basic','Bronze',0.00),
(2,'Silver','Silver',5.00),
(3,'Gold','Gold',10.00),
(4,'Platinum','Platinum',15.00);
/*!40000 ALTER TABLE `loyalty_program` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payment`
--

DROP TABLE IF EXISTS `payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `card_number` varchar(20) DEFAULT NULL,
  `payment_amount` decimal(10,2) NOT NULL,
  `payment_date` date NOT NULL,
  `status` tinyint(4) NOT NULL,
  `client_id` int(11) NOT NULL,
  PRIMARY KEY (`payment_id`),
  KEY `client_id` (`client_id`),
  CONSTRAINT `payment_ibfk_1` FOREIGN KEY (`client_id`) REFERENCES `client` (`client_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment`
--

LOCK TABLES `payment` WRITE;
/*!40000 ALTER TABLE `payment` DISABLE KEYS */;
INSERT INTO `payment` VALUES
(1,'5234567890123456',250.00,'2024-09-10',1,1),
(2,'545678901234567',400.00,'2024-09-11',1,2),
(3,'4456789012345678',600.00,'2024-09-12',0,3),
(4,'4567890123456789',1000.00,'2024-09-13',1,4),
(5,'5678901234567890',275.00,'2024-09-14',1,5),
(6,'5789012345678901',450.00,'2024-09-15',1,6),
(7,'5890123456789012',500.00,'2024-09-16',1,7),
(8,'5901234567890123',550.00,'2024-09-17',0,8),
(9,'4012345678901234',320.00,'2024-09-18',1,9),
(10,'4123456789012345',600.00,'2024-09-19',1,10);
/*!40000 ALTER TABLE `payment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `review`
--

DROP TABLE IF EXISTS `review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `review` (
  `review_id` int(11) NOT NULL AUTO_INCREMENT,
  `rating` int(11) NOT NULL,
  `comment` text DEFAULT NULL,
  `client_id` int(11) NOT NULL,
  `hotel_id` int(11) NOT NULL,
  PRIMARY KEY (`review_id`),
  KEY `client_id` (`client_id`),
  KEY `hotel_id` (`hotel_id`),
  CONSTRAINT `review_ibfk_1` FOREIGN KEY (`client_id`) REFERENCES `client` (`client_id`) ON DELETE CASCADE,
  CONSTRAINT `review_ibfk_2` FOREIGN KEY (`hotel_id`) REFERENCES `hotel` (`hotel_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `review`
--

LOCK TABLES `review` WRITE;
/*!40000 ALTER TABLE `review` DISABLE KEYS */;
INSERT INTO `review` VALUES
(1,4,'Had a pleasant stay.',10,1),
(2,5,'Excellent location and staff.',1,2),
(3,3,'Could be cleaner.',2,3),
(4,4,'Good amenities and comfortable beds.',3,1),
(5,5,'Loved the breakfast!',4,4),
(6,3,'Noise from the street was disturbing.',5,5),
(7,4,'Friendly staff and good service.',6,6),
(8,2,'Room was small and cramped.',7,7),
(9,4,'Nice place, enjoyed the stay.',8,8),
(10,5,'Amazing experience, highly recommend!',9,9),
(11,3,'Decent for the price.',10,10),
(12,4,'Very clean and organized.',1,1);
/*!40000 ALTER TABLE `review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `room`
--

DROP TABLE IF EXISTS `room`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `room` (
  `room_id` int(11) NOT NULL AUTO_INCREMENT,
  `room_type` varchar(45) NOT NULL,
  `price_per_night` decimal(10,2) NOT NULL,
  `available` tinyint(4) NOT NULL,
  `hotel_id` int(11) NOT NULL,
  PRIMARY KEY (`room_id`),
  KEY `hotel_id` (`hotel_id`),
  CONSTRAINT `room_ibfk_1` FOREIGN KEY (`hotel_id`) REFERENCES `hotel` (`hotel_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `room`
--

LOCK TABLES `room` WRITE;
/*!40000 ALTER TABLE `room` DISABLE KEYS */;
INSERT INTO `room` VALUES
(1,'Single',50.00,1,1),
(2,'Double',80.00,1,1),
(3,'Suite',150.00,1,2),
(4,'Deluxe',200.00,1,3),
(5,'Single',55.00,1,4),
(6,'Deluxe',220.00,1,5),
(7,'Double',90.00,1,6),
(8,'Single',60.00,1,7),
(9,'Suite',175.00,1,8),
(10,'Single',65.00,1,9);
/*!40000 ALTER TABLE `room` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-09-26 14:37:24
