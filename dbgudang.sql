-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 03, 2022 at 05:50 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbgudang`
--

-- --------------------------------------------------------

--
-- Table structure for table `barang`
--

CREATE TABLE `barang` (
  `kode_barang` varchar(10) NOT NULL,
  `nama_barang` varchar(50) NOT NULL,
  `satuan` varchar(10) NOT NULL,
  `stok` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `barang`
--

INSERT INTO `barang` (`kode_barang`, `nama_barang`, `satuan`, `stok`) VALUES
('B01', 'PEPSODEN', 'PCS', 40),
('B02', 'LIFEBOY', 'PCS', 30),
('B03', 'INDOMIE', 'DUS', 13),
('B04', 'PULPEN', 'PCS', 10),
('B05', 'WHISKAS', 'PCS', 60),
('B06', 'NUVO', 'PCS', 55);

-- --------------------------------------------------------

--
-- Table structure for table `barang_masuk`
--

CREATE TABLE `barang_masuk` (
  `NO_VOUCHER` varchar(10) NOT NULL,
  `TGL` datetime DEFAULT NULL,
  `KODE_BARANG` varchar(10) DEFAULT NULL,
  `JUMLAH` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `barang_masuk`
--

INSERT INTO `barang_masuk` (`NO_VOUCHER`, `TGL`, `KODE_BARANG`, `JUMLAH`) VALUES
('V001', '2022-12-01 22:35:36', 'B01', 20),
('V002', '2022-12-02 22:35:36', 'B02', 15),
('V003', '2022-12-02 19:25:59', 'B05', 30),
('V004', '2022-12-03 00:00:00', 'B06', 10),
('V005', '2022-12-03 00:00:00', 'B06', 5),
('V006', '2022-12-03 00:00:00', 'B03', 10);

--
-- Triggers `barang_masuk`
--
DELIMITER $$
CREATE TRIGGER `hapus_stok_masuk` AFTER DELETE ON `barang_masuk` FOR EACH ROW BEGIN
	UPDATE barang 
    SET stok=stok - OLD.JUMLAH
	WHERE kode_barang = OLD.kode_barang;
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `input_stok_masuk` AFTER INSERT ON `barang_masuk` FOR EACH ROW BEGIN
	UPDATE barang 
    SET stok=stok + NEW.JUMLAH
	WHERE kode_barang = NEW.kode_barang;
END
$$
DELIMITER ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `barang`
--
ALTER TABLE `barang`
  ADD PRIMARY KEY (`kode_barang`);

--
-- Indexes for table `barang_masuk`
--
ALTER TABLE `barang_masuk`
  ADD PRIMARY KEY (`NO_VOUCHER`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
