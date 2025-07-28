-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 28, 2025 at 03:06 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `phone`
--

-- --------------------------------------------------------

--
-- Table structure for table `list`
--

CREATE TABLE `list` (
  `number` bigint(12) NOT NULL,
  `name` varchar(20) NOT NULL,
  `image` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_persian_ci;

--
-- Dumping data for table `list`
--

INSERT INTO `list` (`number`, `name`, `image`) VALUES
(9332947218, 'hadis', 'C:\\Users\\bcz\\Pictures\\234069.jpg'),
(9123457723, 'noor', 'C:\\Users\\bcz\\Pictures\\234069.jpg'),
(9102657720, 'diyar', 'C:\\Users\\bcz\\Pictures\\234069.jpg'),
(9123225099, 'amir', 'C:\\Users\\bcz\\Pictures\\234069.jpg'),
(9334569987, 'mahdis', 'C:\\Users\\bcz\\Pictures\\234069.jpg'),
(9012309744, 'sarina', 'C:\\Users\\bcz\\Pictures\\234069.jpg'),
(9192467733, 'ava', 'C:\\Users\\bcz\\Pictures\\234069.jpg'),
(9365537789, 'mahoor', 'C:\\Users\\bcz\\Pictures\\234069.jpg');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
