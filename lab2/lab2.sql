-- MySQL Script generated by MySQL Workbench
-- Sun Sep 29 16:20:21 2024
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema lab2
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema lab2
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `lab2` DEFAULT CHARACTER SET utf8 ;
USE `lab2` ;

-- -----------------------------------------------------
-- Table `lab2`.`Product`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab2`.`Product` (
  `maker` VARCHAR(10) NOT NULL,
  `model` VARCHAR(50) NOT NULL unique,
  `type` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`model`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab2`.`PC`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab2`.`PC` (
  `code` INT NOT NULL,
  `speed` SMALLINT NOT NULL,
  `ram` SMALLINT NOT NULL,
  `hd` REAL NOT NULL,
  `cd` VARCHAR(10) NOT NULL,
  `price` INT NOT NULL,
  `model` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`code`, `model`),
  INDEX `fk_PC_Product_idx` (`model` ASC) VISIBLE,
  CONSTRAINT `fk_PC_Product`
    FOREIGN KEY (`model`)
    REFERENCES `lab2`.`Product` (`model`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab2`.`Laptop`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab2`.`Laptop` (
  `code` INT NOT NULL,
  `speed` SMALLINT NOT NULL,
  `ram` SMALLINT NOT NULL,
  `hd` REAL NOT NULL,
  `price` INT NOT NULL,
  `screan` INT NOT NULL,
  `model` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`code`, `model`),
  INDEX `fk_Laptop_Product1_idx` (`model` ASC) VISIBLE,
  CONSTRAINT `fk_Laptop_Product1`
    FOREIGN KEY (`model`)
    REFERENCES `lab2`.`Product` (`model`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `lab2`.`Printer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab2`.`Printer` (
  `code` INT NOT NULL,
  `color` CHAR(1) NOT NULL,
  `type` VARCHAR(10) NOT NULL,
  `price` INT NOT NULL,
  `model` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`code`, `model`),
  INDEX `fk_Printer_Product1_idx` (`model` ASC) VISIBLE,
  CONSTRAINT `fk_Printer_Product1`
    FOREIGN KEY (`model`)
    REFERENCES `lab2`.`Product` (`model`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab2`.`Income_o`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab2`.`Income_o` (
  `point` TINYINT NOT NULL,
  `date` DATE NOT NULL,
  `inc` INT NOT NULL,
  PRIMARY KEY (`point`, `date`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `lab2`.`Outcome_o`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab2`.`Outcome_o` (
  `point` TINYINT NOT NULL,
  `date` DATE NOT NULL,
  `out` INT NOT NULL,
  PRIMARY KEY (`point`, `date`),
  INDEX `fk_Outcome_o_Income_o_idx` (`point`, `date` ASC) VISIBLE,
  CONSTRAINT `fk_Outcome_o_Income_o`
    FOREIGN KEY (`point`, `date`)
    REFERENCES `lab2`.`Income_o` (`point`, `date`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `lab2`.`Income`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab2`.`Income` (
  `code` INT NOT NULL,
  `point` TINYINT NOT NULL,
  `date` DATE NOT NULL,   -- Виправлено тип на DATE
  `inc` INT NOT NULL,
  PRIMARY KEY (`code`),
  INDEX `fk_Income_Income_o_idx` (`point`, `date` ASC) VISIBLE,
  CONSTRAINT `fk_Income_Income_o`
    FOREIGN KEY (`point`, `date`)
    REFERENCES `lab2`.`Income_o` (`point`, `date`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `lab2`.`Outcome`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab2`.`Outcome` (
  `code` INT NOT NULL,
  `point` TINYINT NOT NULL,
  `date` DATE NOT NULL,   -- Виправлено тип на DATE
  `out` INT NOT NULL,
  PRIMARY KEY (`code`),
  INDEX `fk_Outcome_Outcome_o_idx` (`point`, `date` ASC) VISIBLE,
  CONSTRAINT `fk_Outcome_Outcome_o`
    FOREIGN KEY (`point`, `date`)
    REFERENCES `lab2`.`Outcome_o` (`point`, `date`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab2`.`Classes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab2`.`Classes` (
  `class` VARCHAR(50) NOT NULL,
  `type` VARCHAR(2) NOT NULL,
  `country` VARCHAR(50) NOT NULL,
  `numGuns` TINYINT NOT NULL,
  `bore` REAL NOT NULL,
  `displacement` INT NOT NULL,
  PRIMARY KEY (`class`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `lab2`.`Ships`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab2`.`Ships` (
  `name` VARCHAR(50) NOT NULL,
  `class` VARCHAR(50) NOT NULL,
  `launched` INT NOT NULL,
  PRIMARY KEY (`name`),
  INDEX `fk_Ships_Classes_idx` (`class` ASC) VISIBLE,
  CONSTRAINT `fk_Ships_Classes`
    FOREIGN KEY (`class`)
    REFERENCES `lab2`.`Classes` (`class`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `lab2`.`Battles`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab2`.`Battles` (
  `name` VARCHAR(50) NOT NULL,
  `date` DATETIME NOT NULL,
  PRIMARY KEY (`name`, `date`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `lab2`.`Outcomes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab2`.`Outcomes` (
  `ship` VARCHAR(50) NOT NULL,
  `battle` VARCHAR(50) NOT NULL,
  `result` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`ship`, `battle`),
  INDEX `fk_Outcomes_Battles_idx` (`battle` ASC) VISIBLE,
  CONSTRAINT `fk_Outcomes_Battles`
    FOREIGN KEY (`battle`)
    REFERENCES `lab2`.`Battles` (`name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  INDEX `fk_Outcomes_Ships_idx` (`ship` ASC) VISIBLE,
  CONSTRAINT `fk_Outcomes_Ships`
    FOREIGN KEY (`ship`)
    REFERENCES `lab2`.`Ships` (`name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab2`.`Company`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab2`.`Company` (
  `ID_comp` INT NOT NULL,
  `name` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`ID_comp`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `lab2`.`Trip`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab2`.`Trip` (
  `trip_no` INT NOT NULL,
  `ID_comp` INT NOT NULL,
  `plane` VARCHAR(20) NOT NULL,
  `town_from` VARCHAR(100) NOT NULL,
  `town_to` VARCHAR(100) NOT NULL,
  `time_out` TIME NOT NULL,
  `time_in` TIME NOT NULL,
  PRIMARY KEY (`trip_no`),
  INDEX `fk_Trip_Company_idx` (`ID_comp` ASC) VISIBLE,
  CONSTRAINT `fk_Trip_Company`
    FOREIGN KEY (`ID_comp`)
    REFERENCES `lab2`.`Company` (`ID_comp`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `lab2`.`Passenger`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab2`.`Passenger` (
  `ID_psg` INT NOT NULL,
  `name` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`ID_psg`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `lab2`.`Pass_in_trip`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab2`.`Pass_in_trip` (
  `trip_no` INT NOT NULL,
  `date` DATE NOT NULL,
  `ID_psg` INT NOT NULL,
  `place` CHAR(10) NOT NULL,
  PRIMARY KEY (`trip_no`, `date`, `ID_psg`),
  INDEX `fk_Pass_in_trip_Trip_idx` (`trip_no` ASC) VISIBLE,
  INDEX `fk_Pass_in_trip_Passenger_idx` (`ID_psg` ASC) VISIBLE,
  CONSTRAINT `fk_Pass_in_trip_Trip`
    FOREIGN KEY (`trip_no`)
    REFERENCES `lab2`.`Trip` (`trip_no`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Pass_in_trip_Passenger`
    FOREIGN KEY (`ID_psg`)
    REFERENCES `lab2`.`Passenger` (`ID_psg`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Data for table `lab2`.`Product`
-- -----------------------------------------------------
START TRANSACTION;
USE `lab2`;
INSERT INTO `lab2`.`Product` (`maker`, `model`, `type`) VALUES ('B', 1121, 'PC');
INSERT INTO `lab2`.`Product` (`maker`, `model`, `type`) VALUES ('A', 1232, 'PC');
INSERT INTO `lab2`.`Product` (`maker`, `model`, `type`) VALUES ('A', 1233, 'PC');
INSERT INTO `lab2`.`Product` (`maker`, `model`, `type`) VALUES ('E', 1260, 'PC');
INSERT INTO `lab2`.`Product` (`maker`, `model`, `type`) VALUES ('A', 1276, 'Printer');
INSERT INTO `lab2`.`Product` (`maker`, `model`, `type`) VALUES ('D', 1288, 'Printer');
INSERT INTO `lab2`.`Product` (`maker`, `model`, `type`) VALUES ('A', 1298, 'Laptop');
INSERT INTO `lab2`.`Product` (`maker`, `model`, `type`) VALUES ('C', 1321, 'Laptop');
INSERT INTO `lab2`.`Product` (`maker`, `model`, `type`) VALUES ('A', 1401, 'Printer');
INSERT INTO `lab2`.`Product` (`maker`, `model`, `type`) VALUES ('A', 1408, 'Printer');
INSERT INTO `lab2`.`Product` (`maker`, `model`, `type`) VALUES ('D', 1433, 'Printer');
INSERT INTO `lab2`.`Product` (`maker`, `model`, `type`) VALUES ('E', 1434, 'Printer');
INSERT INTO `lab2`.`Product` (`maker`, `model`, `type`) VALUES ('B', 1750, 'Laptop');
INSERT INTO `lab2`.`Product` (`maker`, `model`, `type`) VALUES ('A', 1752, 'Laptop');
INSERT INTO `lab2`.`Product` (`maker`, `model`, `type`) VALUES ('E', 2111, 'PC');
INSERT INTO `lab2`.`Product` (`maker`, `model`, `type`) VALUES ('E', 2112, 'PC');
COMMIT;


-- -----------------------------------------------------
-- Data for table `lab2`.`Laptop`
-- -----------------------------------------------------
START TRANSACTION;
USE `lab2`;
INSERT INTO `lab2`.`Laptop` (`code`, `speed`, `ram`, `hd`, `price`, `screen`, `model`) VALUES (1, 350, 32, 4, 700.00, 11, '1298');
INSERT INTO `lab2`.`Laptop` (`code`, `speed`, `ram`, `hd`, `price`, `screen`, `model`) VALUES (2, 500, 64, 8, 970.00, 12, '1321');
INSERT INTO `lab2`.`Laptop` (`code`, `speed`, `ram`, `hd`, `price`, `screen`, `model`) VALUES (3, 750, 128, 12, 1200.00, 14, '1750');
INSERT INTO `lab2`.`Laptop` (`code`, `speed`, `ram`, `hd`, `price`, `screen`, `model`) VALUES (4, 600, 64, 10, 1050.00, 15, '1298');
INSERT INTO `lab2`.`Laptop` (`code`, `speed`, `ram`, `hd`, `price`, `screen`, `model`) VALUES (5, 750, 128, 10, 1150.00, 14, '1752');
INSERT INTO `lab2`.`Laptop` (`code`, `speed`, `ram`, `hd`, `price`, `screen`, `model`) VALUES (6, 450, 64, 10, 950.00, 12, '1298');
COMMIT;


-- -----------------------------------------------------
-- Data for table `lab2`.`PC`
-- -----------------------------------------------------
START TRANSACTION;
USE `lab2`;

-- Ensure `code` and `model` are unique
INSERT INTO `lab2`.`PC` (`code`, `speed`, `ram`, `hd`, `cd`, `price`, `model`) VALUES (1, 500, 64, 5, '12x', 600.00, '1232');
INSERT INTO `lab2`.`PC` (`code`, `speed`, `ram`, `hd`, `cd`, `price`, `model`) VALUES (2, 750, 128, 14, '40x', 850.00, '1121');
INSERT INTO `lab2`.`PC` (`code`, `speed`, `ram`, `hd`, `cd`, `price`, `model`) VALUES (3, 500, 64, 5, '12x', 600.00, '1233');
INSERT INTO `lab2`.`PC` (`code`, `speed`, `ram`, `hd`, `cd`, `price`, `model`) VALUES (4, 600, 128, 14, '40x', 850.00, '1122');
INSERT INTO `lab2`.`PC` (`code`, `speed`, `ram`, `hd`, `cd`, `price`, `model`) VALUES (5, 600, 128, 8, '40x', 850.00, '1123');
INSERT INTO `lab2`.`PC` (`code`, `speed`, `ram`, `hd`, `cd`, `price`, `model`) VALUES (6, 750, 128, 20, '50x', 950.00, '1233');
INSERT INTO `lab2`.`PC` (`code`, `speed`, `ram`, `hd`, `cd`, `price`, `model`) VALUES (7, 500, 32, 10, '12x', 400.00, '1232');
INSERT INTO `lab2`.`PC` (`code`, `speed`, `ram`, `hd`, `cd`, `price`, `model`) VALUES (8, 450, 64, 8, '24x', 350.00, '1232');
INSERT INTO `lab2`.`PC` (`code`, `speed`, `ram`, `hd`, `cd`, `price`, `model`) VALUES (9, 450, 32, 10, '24x', 350.00, '1232');
INSERT INTO `lab2`.`PC` (`code`, `speed`, `ram`, `hd`, `cd`, `price`, `model`) VALUES (10, 500, 32, 10, '12x', 350.00, '1260');
INSERT INTO `lab2`.`PC` (`code`, `speed`, `ram`, `hd`, `cd`, `price`, `model`) VALUES (11, 900, 128, 40, '40x', 980.00, '1233');
COMMIT;


-- -----------------------------------------------------
-- Data for table `lab2`.`Printer`
-- -----------------------------------------------------
START TRANSACTION;
USE `lab2`;
INSERT INTO `lab2`.`Printer` (`code`, `color`, `type`, `price`, `model`) VALUES (1, 'n', 'Laser', 400.00, '1276');
INSERT INTO `lab2`.`Printer` (`code`, `color`, `type`, `price`, `model`) VALUES (2, 'y', 'Jet', 270.00, '1433');
INSERT INTO `lab2`.`Printer` (`code`, `color`, `type`, `price`, `model`) VALUES (3, 'y', 'Jet', 290.00, '1434');
INSERT INTO `lab2`.`Printer` (`code`, `color`, `type`, `price`, `model`) VALUES (4, 'n', 'Matrix', 150.00, '1401');
INSERT INTO `lab2`.`Printer` (`code`, `color`, `type`, `price`, `model`) VALUES (5, 'n', 'Matrix', 270.00, '1408');
INSERT INTO `lab2`.`Printer` (`code`, `color`, `type`, `price`, `model`) VALUES (6, 'n', 'Laser', 400.00, '1288');
COMMIT;


-- -----------------------------------------------------
-- Data for table `lab2`.`Income_o`
-- -----------------------------------------------------
START TRANSACTION;
USE `lab2`;
INSERT INTO `lab2`.`Income_o` (`point`, `date`, `inc`) VALUES (1, '2001-03-22', 15000.00);
INSERT INTO `lab2`.`Income_o` (`point`, `date`, `inc`) VALUES (2, '2001-03-23', 15000.00);
INSERT INTO `lab2`.`Income_o` (`point`, `date`, `inc`) VALUES (1, '2001-03-24', 3400.00);
INSERT INTO `lab2`.`Income_o` (`point`, `date`, `inc`) VALUES (1, '2001-04-13', 5000.00);
INSERT INTO `lab2`.`Income_o` (`point`, `date`, `inc`) VALUES (1, '2001-05-11', 4500.00);
INSERT INTO `lab2`.`Income_o` (`point`, `date`, `inc`) VALUES (2, '2001-03-22', 10000.00);
INSERT INTO `lab2`.`Income_o` (`point`, `date`, `inc`) VALUES (1, '2001-03-24', 1500.00);
INSERT INTO `lab2`.`Income_o` (`point`, `date`, `inc`) VALUES (3, '2001-09-13', 11500.00);
INSERT INTO `lab2`.`Income_o` (`point`, `date`, `inc`) VALUES (3, '2001-10-02', 18000.00);
COMMIT;

-- -----------------------------------------------------
-- Data for table `lab2`.`Outcome_o`
-- -----------------------------------------------------
START TRANSACTION;
USE `lab2`;
INSERT INTO `lab2`.`Outcome_o` (`point`, `date`, `out`) VALUES (1, '2001-03-14', 15348.00);
INSERT INTO `lab2`.`Outcome_o` (`point`, `date`, `out`) VALUES (1, '2001-03-24', 3663.00);
INSERT INTO `lab2`.`Outcome_o` (`point`, `date`, `out`) VALUES (1, '2001-03-26', 1221.00);
INSERT INTO `lab2`.`Outcome_o` (`point`, `date`, `out`) VALUES (1, '2001-03-28', 2075.00);
INSERT INTO `lab2`.`Outcome_o` (`point`, `date`, `out`) VALUES (1, '2001-03-29', 2004.00);
INSERT INTO `lab2`.`Outcome_o` (`point`, `date`, `out`) VALUES (1, '2001-04-11', 3195.04);
INSERT INTO `lab2`.`Outcome_o` (`point`, `date`, `out`) VALUES (1, '2001-04-13', 4490.00);
INSERT INTO `lab2`.`Outcome_o` (`point`, `date`, `out`) VALUES (1, '2001-04-27', 3110.00);
INSERT INTO `lab2`.`Outcome_o` (`point`, `date`, `out`) VALUES (1, '2001-05-11', 2530.00);
INSERT INTO `lab2`.`Outcome_o` (`point`, `date`, `out`) VALUES (1, '2001-03-22', 1440.00);
INSERT INTO `lab2`.`Outcome_o` (`point`, `date`, `out`) VALUES (2, '2001-03-29', 7848.00);
INSERT INTO `lab2`.`Outcome_o` (`point`, `date`, `out`) VALUES (3, '2001-09-13', 2040.00);
INSERT INTO `lab2`.`Outcome_o` (`point`, `date`, `out`) VALUES (1, '2001-03-24', 3500.00);
INSERT INTO `lab2`.`Outcome_o` (`point`, `date`, `out`) VALUES (2, '2001-03-29', 2006.00);
INSERT INTO `lab2`.`Outcome_o` (`point`, `date`, `out`) VALUES (3, '2001-09-19', 2300.00);
INSERT INTO `lab2`.`Outcome_o` (`point`, `date`, `out`) VALUES (3, '2002-09-16', 2150.00);
COMMIT;

-- -----------------------------------------------------
-- Data for table `lab2`.`Income`
-- -----------------------------------------------------
START TRANSACTION;
USE `lab2`;
INSERT INTO `lab2`.`Income` (`code`, `point`, `date`, `inc`) VALUES (1, 1, '2001-03-22 00:00:00', 15000.00);
INSERT INTO `lab2`.`Income` (`code`, `point`, `date`, `inc`) VALUES (2, 1, '2001-03-23 00:00:00', 15000.00);
INSERT INTO `lab2`.`Income` (`code`, `point`, `date`, `inc`) VALUES (3, 1, '2001-03-24 00:00:00', 3600.00);
INSERT INTO `lab2`.`Income` (`code`, `point`, `date`, `inc`) VALUES (4, 2, '2001-03-22 00:00:00', 10000.00);
INSERT INTO `lab2`.`Income` (`code`, `point`, `date`, `inc`) VALUES (5, 1, '2001-03-24 00:00:00', 1500.00);
INSERT INTO `lab2`.`Income` (`code`, `point`, `date`, `inc`) VALUES (6, 1, '2001-04-13 00:00:00', 5000.00);
INSERT INTO `lab2`.`Income` (`code`, `point`, `date`, `inc`) VALUES (7, 1, '2001-05-11 00:00:00', 4500.00);
INSERT INTO `lab2`.`Income` (`code`, `point`, `date`, `inc`) VALUES (8, 1, '2001-03-22 00:00:00', 15000.00);
INSERT INTO `lab2`.`Income` (`code`, `point`, `date`, `inc`) VALUES (9, 1, '2001-03-24 00:00:00', 1500.00);
INSERT INTO `lab2`.`Income` (`code`, `point`, `date`, `inc`) VALUES (10, 1, '2001-04-13 00:00:00', 5000.00);
INSERT INTO `lab2`.`Income` (`code`, `point`, `date`, `inc`) VALUES (11, 1, '2001-03-24 00:00:00', 3400.00);
INSERT INTO `lab2`.`Income` (`code`, `point`, `date`, `inc`) VALUES (12, 3, '2001-09-13 00:00:00', 1350.00);
INSERT INTO `lab2`.`Income` (`code`, `point`, `date`, `inc`) VALUES (13, 3, '2001-09-13 00:00:00', 1750.00);
COMMIT;

-- -----------------------------------------------------
-- Data for table `lab2`.`Outcome`
-- -----------------------------------------------------
START TRANSACTION;
USE `lab2`;
INSERT INTO `lab2`.`Outcome` (`code`, `point`, `date`, `out`) VALUES (1, 1, '2001-03-14 00:00:00', 15348.00);
INSERT INTO `lab2`.`Outcome` (`code`, `point`, `date`, `out`) VALUES (2, 1, '2001-03-24 00:00:00', 3663.00);
INSERT INTO `lab2`.`Outcome` (`code`, `point`, `date`, `out`) VALUES (3, 1, '2001-03-26 00:00:00', 1221.00);
INSERT INTO `lab2`.`Outcome` (`code`, `point`, `date`, `out`) VALUES (4, 1, '2001-03-28 00:00:00', 2075.00);
INSERT INTO `lab2`.`Outcome` (`code`, `point`, `date`, `out`) VALUES (5, 1, '2001-03-29 00:00:00', 2004.00);
INSERT INTO `lab2`.`Outcome` (`code`, `point`, `date`, `out`) VALUES (6, 1, '2001-04-11 00:00:00', 3195.04);
INSERT INTO `lab2`.`Outcome` (`code`, `point`, `date`, `out`) VALUES (7, 1, '2001-04-13 00:00:00', 4490.00);
INSERT INTO `lab2`.`Outcome` (`code`, `point`, `date`, `out`) VALUES (8, 1, '2001-04-27 00:00:00', 3110.00);
INSERT INTO `lab2`.`Outcome` (`code`, `point`, `date`, `out`) VALUES (9, 1, '2001-05-11 00:00:00', 2530.00);
INSERT INTO `lab2`.`Outcome` (`code`, `point`, `date`, `out`) VALUES (10, 1, '2001-03-22 00:00:00', 1440.00);
INSERT INTO `lab2`.`Outcome` (`code`, `point`, `date`, `out`) VALUES (11, 2, '2001-03-29 00:00:00', 7848.00);
INSERT INTO `lab2`.`Outcome` (`code`, `point`, `date`, `out`) VALUES (12, 3, '2001-04-02 00:00:00', 2040.00);
INSERT INTO `lab2`.`Outcome` (`code`, `point`, `date`, `out`) VALUES (13, 1, '2001-03-24 00:00:00', 3500.00);
INSERT INTO `lab2`.`Outcome` (`code`, `point`, `date`, `out`) VALUES (14, 1, '2001-03-22 00:00:00', 1440.00);
INSERT INTO `lab2`.`Outcome` (`code`, `point`, `date`, `out`) VALUES (15, 1, '2001-03-29 00:00:00', 2006.00);
INSERT INTO `lab2`.`Outcome` (`code`, `point`, `date`, `out`) VALUES (16, 3, '2001-09-19 00:00:00', 1500.00);
INSERT INTO `lab2`.`Outcome` (`code`, `point`, `date`, `out`) VALUES (17, 3, '2001-09-19 00:00:00', 2300.00);
INSERT INTO `lab2`.`Outcome` (`code`, `point`, `date`, `out`) VALUES (18, 3, '2001-09-14 00:00:00', 1150.00);
COMMIT;


-- -----------------------------------------------------
-- Data for table `lab2`.`Classes`
-- -----------------------------------------------------
START TRANSACTION;
USE `lab2`;
INSERT INTO `lab2`.`Classes` (`class`, `type`, `country`, `numGuns`, `bore`, `displacement`) 
VALUES ('Bismarck', 'bb', 'Germany', 8, 15, 42000);
INSERT INTO `lab2`.`Classes` (`class`, `type`, `country`, `numGuns`, `bore`, `displacement`) 
VALUES ('Iowa', 'bb', 'USA', 9, 16, 46000);
INSERT INTO `lab2`.`Classes` (`class`, `type`, `country`, `numGuns`, `bore`, `displacement`) 
VALUES ('Kongo', 'bc', 'Japan', 8, 14, 32000);
INSERT INTO `lab2`.`Classes` (`class`, `type`, `country`, `numGuns`, `bore`, `displacement`) 
VALUES ('North Carolina', 'bb', 'USA', 12, 16, 37000);
INSERT INTO `lab2`.`Classes` (`class`, `type`, `country`, `numGuns`, `bore`, `displacement`) 
VALUES ('Renown', 'bc', 'GB', 6, 15, 32000);
INSERT INTO `lab2`.`Classes` (`class`, `type`, `country`, `numGuns`, `bore`, `displacement`) 
VALUES ('Revenge', 'bb', 'GB', 8, 15, 29000);
INSERT INTO `lab2`.`Classes` (`class`, `type`, `country`, `numGuns`, `bore`, `displacement`) 
VALUES ('Tennessee', 'bb', 'USA', 12, 14, 32000);
INSERT INTO `lab2`.`Classes` (`class`, `type`, `country`, `numGuns`, `bore`, `displacement`) 
VALUES ('Yamato', 'bb', 'Japan', 9, 18, 65000);
COMMIT;

-- -----------------------------------------------------
-- Data for table `lab2`.`Ships`
-- -----------------------------------------------------
START TRANSACTION;
USE `lab2`;
INSERT INTO `lab2`.`Ships` (`name`, `class`, `launched`) 
VALUES ('California', 'Tennessee', 1921);
INSERT INTO `lab2`.`Ships` (`name`, `class`, `launched`) 
VALUES ('Haruna', 'Kongo', 1916);
INSERT INTO `lab2`.`Ships` (`name`, `class`, `launched`) 
VALUES ('Hiei', 'Kongo', 1914);
INSERT INTO `lab2`.`Ships` (`name`, `class`, `launched`) 
VALUES ('Iowa', 'Iowa', 1943);
INSERT INTO `lab2`.`Ships` (`name`, `class`, `launched`) 
VALUES ('Kirishima', 'Kongo', 1915);
INSERT INTO `lab2`.`Ships` (`name`, `class`, `launched`) 
VALUES ('Missouri', 'Iowa', 1944);
INSERT INTO `lab2`.`Ships` (`name`, `class`, `launched`) 
VALUES ('Musashi', 'Yamato', 1942);
INSERT INTO `lab2`.`Ships` (`name`, `class`, `launched`) 
VALUES ('New Jersey', 'Iowa', 1943);
INSERT INTO `lab2`.`Ships` (`name`, `class`, `launched`) 
VALUES ('North Carolina', 'North Carolina', 1941);
INSERT INTO `lab2`.`Ships` (`name`, `class`, `launched`) 
VALUES ('Ramillies', 'Revenge', 1917);
INSERT INTO `lab2`.`Ships` (`name`, `class`, `launched`) 
VALUES ('Renown', 'Renown', 1916);
INSERT INTO `lab2`.`Ships` (`name`, `class`, `launched`) 
VALUES ('Repulse', 'Renown', 1916);
INSERT INTO `lab2`.`Ships` (`name`, `class`, `launched`) 
VALUES ('Resolution', 'Renown', 1916);
INSERT INTO `lab2`.`Ships` (`name`, `class`, `launched`) 
VALUES ('Revenge', 'Revenge', 1916);
INSERT INTO `lab2`.`Ships` (`name`, `class`, `launched`) 
VALUES ('Royal Oak', 'Revenge', 1916);
INSERT INTO `lab2`.`Ships` (`name`, `class`, `launched`) 
VALUES ('Royal Sovereign', 'Revenge', 1916);
INSERT INTO `lab2`.`Ships` (`name`, `class`, `launched`) 
VALUES ('South Dakota', 'North Carolina', 1941);
INSERT INTO `lab2`.`Ships` (`name`, `class`, `launched`) 
VALUES ('Tennessee', 'Tennessee', 1920);
INSERT INTO `lab2`.`Ships` (`name`, `class`, `launched`) 
VALUES ('Washington', 'North Carolina', 1941);
INSERT INTO `lab2`.`Ships` (`name`, `class`, `launched`) 
VALUES ('Wisconsin', 'Iowa', 1944);
INSERT INTO `lab2`.`Ships` (`name`, `class`, `launched`) 
VALUES ('Yamato', 'Yamato', 1941);
COMMIT;

-- -----------------------------------------------------
-- Data for table `lab2`.`Battles`
-- -----------------------------------------------------
START TRANSACTION;
USE `lab2`;
INSERT INTO `lab2`.`Battles` (`name`, `date`) 
VALUES ('#Cuba62a', '1962-10-20 00:00:00');
INSERT INTO `lab2`.`Battles` (`name`, `date`) 
VALUES ('#Cuba62b', '1962-10-25 00:00:00');
INSERT INTO `lab2`.`Battles` (`name`, `date`) 
VALUES ('Guadalcanal', '1942-11-15 00:00:00');
INSERT INTO `lab2`.`Battles` (`name`, `date`) 
VALUES ('North Atlantic', '1941-05-25 00:00:00');
INSERT INTO `lab2`.`Battles` (`name`, `date`) 
VALUES ('North Cape', '1943-12-26 00:00:00');
INSERT INTO `lab2`.`Battles` (`name`, `date`) 
VALUES ('Surigao Strait', '1944-10-25 00:00:00');
COMMIT;

-- -----------------------------------------------------
-- Data for table `lab2`.`Outcomes`
-- -----------------------------------------------------
START TRANSACTION;
USE `lab2`;
INSERT INTO `lab2`.`Outcomes` (`ship`, `battle`, `result`) 
VALUES ('Bismarck', 'North Atlantic', 'sunk');
INSERT INTO `lab2`.`Outcomes` (`ship`, `battle`, `result`) 
VALUES ('California', 'Guadalcanal', 'damaged');
INSERT INTO `lab2`.`Outcomes` (`ship`, `battle`, `result`) 
VALUES ('California', 'Guadalcanal', 'damaged');
INSERT INTO `lab2`.`Outcomes` (`ship`, `battle`, `result`) 
VALUES ('Duke of York', 'North Cape', 'OK');
INSERT INTO `lab2`.`Outcomes` (`ship`, `battle`, `result`) 
VALUES ('Fuso', 'Surigao Strait', 'sunk');
INSERT INTO `lab2`.`Outcomes` (`ship`, `battle`, `result`) 
VALUES ('Hood', 'North Atlantic', 'sunk');
INSERT INTO `lab2`.`Outcomes` (`ship`, `battle`, `result`) 
VALUES ('King George V', 'North Atlantic', 'OK');
INSERT INTO `lab2`.`Outcomes` (`ship`, `battle`, `result`) 
VALUES ('Kirishima', 'Guadalcanal', 'sunk');
INSERT INTO `lab2`.`Outcomes` (`ship`, `battle`, `result`) 
VALUES ('Prince of Wales', 'North Atlantic', 'damaged');
INSERT INTO `lab2`.`Outcomes` (`ship`, `battle`, `result`) 
VALUES ('Rodney', 'North Atlantic', 'OK');
INSERT INTO `lab2`.`Outcomes` (`ship`, `battle`, `result`) 
VALUES ('Scharnhorst', 'North Cape', 'sunk');
INSERT INTO `lab2`.`Outcomes` (`ship`, `battle`, `result`) 
VALUES ('South Dakota', 'Guadalcanal', 'damaged');
INSERT INTO `lab2`.`Outcomes` (`ship`, `battle`, `result`) 
VALUES ('Tennessee', 'Surigao Strait', 'OK');
INSERT INTO `lab2`.`Outcomes` (`ship`, `battle`, `result`) 
VALUES ('West Virginia', 'Surigao Strait', 'OK');
INSERT INTO `lab2`.`Outcomes` (`ship`, `battle`, `result`) 
VALUES ('Yamashiro', 'Surigao Strait', 'sunk');
COMMIT;


-- -----------------------------------------------------
-- Data for table `lab2`.`Company`
-- -----------------------------------------------------
INSERT INTO lab2.Company (ID_comp, name)
VALUES 
(1, 'Don_avia'),
(2, 'Aeroflot'),
(3, 'Dale_avia'),
(4, 'air_France'),
(5, 'British_AW');

-- -----------------------------------------------------
-- Data for table `lab2`.`Trip`
-- -----------------------------------------------------
INSERT INTO lab2.Trip (trip_no, ID_comp, plane, town_from, town_to, time_out, time_in)
VALUES 
(1100, 1, 'Boeing', 'Rostov', 'Paris', '14:30:00', '17:50:00'),
(1101, 4, 'Boeing', 'Paris', 'Rostov', '12:00:00', '14:00:00'),
(1123, 3, 'TU-154', 'Rostov', 'Vladivost', '16:20:00', '18:40:00'),
(1124, 3, 'TU-154', 'Rostov', 'Vladivost', '17:30:00', '19:50:00'),
(1145, 2, 'IL-86', 'Moscow', 'Rostov', '19:00:00', '21:20:00'),
(1146, 2, 'IL-86', 'Moscow', 'Rostov', '20:00:00', '22:20:00'),
(1181, 2, 'TU-134', 'Moscow', 'Rostov', '16:30:00', '18:50:00'),
(1182, 2, 'TU-134', 'Moscow', 'Rostov', '17:00:00', '19:20:00'),
(7771, 5, 'Boeing', 'London', 'Singapore', '22:00:00', '05:00:00'),
(7772, 5, 'Boeing', 'London', 'Singapore', '20:00:00', '03:00:00'),
(7773, 5, 'Boeing', 'Singapore', 'London', '01:00:00', '06:00:00'),
(7774, 5, 'Boeing', 'Singapore', 'London', '02:00:00', '07:00:00'),
(7775, 5, 'Boeing', 'London', 'Paris', '23:00:00', '01:00:00'),
(8882, 5, 'Boeing', 'Paris', 'London', '21:00:00', '23:00:00');

-- -----------------------------------------------------
-- Data for table `lab2`.`Passenger`
-- -----------------------------------------------------
INSERT INTO lab2.Passenger (ID_psg, name)
VALUES 
(1, 'Bruce Willis'),
(2, 'George Clooney'),
(3, 'Kevin Costner'),
(4, 'Donald Sutherland'),
(5, 'Jennifer Lopez'),
(6, 'Ray Liotta'),
(7, 'Samuel L. Jackson'),
(8, 'Nicole Kidman'),
(9, 'Alan Rickman'),
(10, 'Kurt Russell'),
(11, 'Harrison Ford'),
(12, 'Russell Crowe'),
(13, 'Steve Martin'),
(14, 'Tom Hanks'),
(15, 'Angelina Jolie'),
(16, 'Mel Gibson'),
(17, 'Michael Douglas'),
(18, 'John Travolta'),
(19, 'Sylvester Stallone'),
(20, 'Tommy Lee Jones'),
(21, 'Catherine Zeta-Jones'),
(22, 'Antonio Banderas'),
(23, 'Kim Basinger'),
(24, 'Sam Neill'),
(25, 'Gary Oldman'),
(26, 'Clint Eastwood'),
(27, 'Brad Pitt'),
(28, 'Johnny Depp'),
(29, 'Pierce Brosnan'),
(30, 'Sean Connery'),
(31, 'Bruce Lee'),
(32, 'Mullah Omar');

INSERT INTO lab2.Pass_in_trip (trip_no, date, ID_psg, place)
VALUES 
(1100, '2003-04-29', 1, '1a'),
(1123, '2003-04-08', 3, '2a'),
(1123, '2003-04-08', 1, '4c'),
(1123, '2003-04-08', 5, '4b'),
(1124, '2003-04-01', 2, '1b'),
(1145, '2003-04-08', 3, '2d'),
(1145, '2003-04-25', 6, '1a'),
(1181, '2003-04-01', 1, '1a'),
(1181, '2003-04-01', 6, '1b'),
(1182, '2003-04-13', 9, '6d'),
(1182, '2003-04-13', 5, '4b'),
(1187, '2003-04-14', 8, '3a'),
(1187, '2003-04-14', 10, '3d'),
(1188, '2003-04-01', 8, '3a'),
(7771, '2005-11-04', 11, '1b'),
(7771, '2005-11-07', 11, '1c'),
(7771, '2005-11-14', 11, '4d'),
(7771, '2005-11-16', 14, '5d'),
(7772, '2005-11-07', 12, '1d'),
(7772, '2005-11-07', 37, '1a'),
(7772, '2005-11-29', 10, '3a'),
(7772, '2005-11-29', 13, '1b'),
(7773, '2005-11-08', 14, '1c'),
(7774, '2005-11-08', 10, '2a'),
(7778, '2005-11-05', 10, '2a'),
(8881, '2005-11-08', 37, '1d'),
(8882, '2005-11-06', 37, '1a'),
(8882, '2005-11-13', 14, '3d');


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
