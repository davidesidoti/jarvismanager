-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Set 08, 2023 alle 17:53
-- Versione del server: 10.4.28-MariaDB
-- Versione PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `test_jarvismanager`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `categories`
--

CREATE TABLE `categories` (
  `id` int(11) NOT NULL,
  `category` mediumtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `categories`
--

INSERT INTO `categories` (`id`, `category`) VALUES
(1, 'social'),
(2, 'games');

-- --------------------------------------------------------

--
-- Struttura della tabella `passwords`
--

CREATE TABLE `passwords` (
  `id` int(11) NOT NULL,
  `category_id` int(11) DEFAULT NULL,
  `name` mediumtext NOT NULL,
  `url` longtext NOT NULL,
  `user` mediumtext NOT NULL,
  `password` mediumtext NOT NULL,
  `creation_date` datetime NOT NULL DEFAULT current_timestamp(),
  `update_date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `passwords`
--

INSERT INTO `passwords` (`id`, `category_id`, `name`, `url`, `user`, `password`, `creation_date`, `update_date`) VALUES
(1, 1, 'instagram', 'https://instagram.com/login', 'sidotidavide@gmail.com', 'InstaTest1234', '2023-09-08 15:53:57', '2023-09-08 15:53:57'),
(2, 1, 'tiktok', 'https://tiktok.com/login', 'sidotidavide@gmail.com', 'TkTkTest1234', '2023-09-08 15:53:57', '2023-09-08 15:53:57'),
(3, 2, 'riot', 'https://riot.com/login', 'sidotidavide@gmail.com', 'ValoUnoTest1234', '2023-09-08 15:54:51', '2023-09-08 15:54:51'),
(4, 2, 'riot', 'https://riot.com/login', 'd.sidoti@gmail.com', 'ValoDueTest1234', '2023-09-08 15:54:51', '2023-09-08 15:54:51'),
(5, 2, 'steam', 'https://steam.com/login', 'sidotidavide@gmail.com', 'SteamTest1234', '2023-09-08 15:55:16', '2023-09-08 15:55:16');

-- --------------------------------------------------------

--
-- Struttura della tabella `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` text DEFAULT NULL,
  `surname` text DEFAULT NULL,
  `username` mediumtext DEFAULT NULL,
  `email` mediumtext NOT NULL,
  `password` mediumtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `users`
--

INSERT INTO `users` (`id`, `name`, `surname`, `username`, `email`, `password`) VALUES
(1, 'Davide', 'Sidoti', 'hash', 'sidotidavide@gmail.com', '$2b$12$OwLsmPTQs4CHLfj9Bj7lTOW08n639hT.MzSvT5N.nf1F/rcSngOIK');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`id`);

--
-- Indici per le tabelle `passwords`
--
ALTER TABLE `passwords`
  ADD PRIMARY KEY (`id`);

--
-- Indici per le tabelle `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `categories`
--
ALTER TABLE `categories`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT per la tabella `passwords`
--
ALTER TABLE `passwords`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT per la tabella `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
