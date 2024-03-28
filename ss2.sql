-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 15, 2023 at 03:55 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ss2`
--
CREATE DATABASE IF NOT EXISTS `ss2` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `ss2`;

-- --------------------------------------------------------

--
-- Table structure for table `grammar`
--

DROP TABLE IF EXISTS `grammar`;
CREATE TABLE IF NOT EXISTS `grammar` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `text` longtext DEFAULT NULL,
  `answer` longtext DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `grammar`
--

INSERT INTO `grammar` (`id`, `user_id`, `text`, `answer`) VALUES
(3, 38, 'Hello my name u Quoc An ans i have a dog.', 'Hello, my name is Quoc An and I have a dog.'),
(5, 38, 'I likes this dogn so muchssa.', 'I like this dog so much.'),
(7, 38, 'With its focusns on personalized recommendations, community engagement, andda user-friendly design, MusiiGroove has the potential to become thee gos-to app for music lovers worldwide. Get ready to embark on an exciting journey intof the world of music with MusiiGroove.', 'With its focus on personalized recommendations, community engagement, and a user-friendly design, MusiiGroove has the potential to become the go-to app for music lovers worldwide. Get ready to embark on an exciting journey into the world of music with MusiiGroove.');

-- --------------------------------------------------------

--
-- Table structure for table `paraphrase`
--

DROP TABLE IF EXISTS `paraphrase`;
CREATE TABLE IF NOT EXISTS `paraphrase` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `text` longtext DEFAULT NULL,
  `answer` longtext DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `paraphrase`
--

INSERT INTO `paraphrase` (`id`, `user_id`, `text`, `answer`) VALUES
(3, 38, 'Hello, my name is Quoc An.', 'Greetings, I am Quoc An., I am from Vietnam. Hi, I\'m Quoc An and I\'m from Vietnam., Hi, I am Quoc An.');

-- --------------------------------------------------------

--
-- Table structure for table `plagiarism`
--

DROP TABLE IF EXISTS `plagiarism`;
CREATE TABLE IF NOT EXISTS `plagiarism` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `text` longtext DEFAULT NULL,
  `answer` longtext DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `plagiarism`
--

INSERT INTO `plagiarism` (`id`, `user_id`, `text`, `answer`) VALUES
(1, 38, 'Social media platforms, like Instagram or Facebook, have been around for years. As soon as their features allowed us to move beyond a limited circle of friends, we started using them to promote ourselves online.', 'https://www.ielts-mentor.com/writing-sample/writing-task-2/983-the-way-many-people-interact-with-each-other-has-changed (Similarity: 34.78%)\nhttps://www.theatlantic.com/technology/archive/2022/11/twitter-facebook-social-media-decline/672074/ (Similarity: 22.58%)\nhttps://bandcamp.com/guide (Similarity: 22.09%)\nhttps://www.samhsa.gov/sites/default/files/programs_campaigns/brss_tacs/samhsa-storytelling-guide.pdf (Similarity: 21.51%)\nhttps://ieltsonlinetests.com/essay-samples/writing-task-2-question-essay-writing-evaluation-band-8 (Similarity: 21.28%)\nhttps://www.womenshealthmag.com/relationships/g38736242/best-dating-app/ (Similarity: 21.0%)\nhttps://effectiviology.com/dangers-of-social-media/ (Similarity: 19.05%)\nhttps://journals.sagepub.com/doi/10.1177/2056305120912488 (Similarity: 18.45%)\nhttps://www.coursesidekick.com/marketing/study-guides/boundless-marketing/introduction-to-social-media-and-digital-marketing (Similarity: 18.45%)\nhttps://www.intechopen.com/chapters/70973 (Similarity: 18.0%)');

-- --------------------------------------------------------

--
-- Table structure for table `textcomplete`
--

DROP TABLE IF EXISTS `textcomplete`;
CREATE TABLE IF NOT EXISTS `textcomplete` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `text` longtext DEFAULT NULL,
  `answer` longtext DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `textcomplete`
--

INSERT INTO `textcomplete` (`id`, `user_id`, `text`, `answer`) VALUES
(1, 38, 'Hello', 'Hello everyone,\n\nIt\'s been a while since we\'ve seen each other, and I\'m sure everyone has been busy in their own ways. But now, it\'s time to come together and make a difference in our community. We have the power to make a real impact, and I\'m confident t'),
(4, 38, 'Hello', 'Hello ,\n\nI\'m so glad that you are here! It\'s been a long time since I\'ve felt this kind of excitement, and I can\'t wait to see what amazing things we can do together. I\'m sure that the sky is the limit, and I\'m confident that our creative minds will be able to come up with something truly unique. With our combined talents, I\'m sure that we can create something that will be remembered for years to come. Let\'s work together and make something that will be remembered for generations!');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `image` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `email`, `image`, `password`) VALUES
(38, 'An Quốc', 'quocann202@gmail.com', 'https://lh3.googleusercontent.com/a/AGNmyxYPnr-2zLFyGe2S9cyreK1pYlfk3FxLnC6frgElcw=s96-c', ''),
(39, 'Quốc An 1C-20CACN', '2001140001@s.hanu.edu.vn', 'https://lh3.googleusercontent.com/a/AGNmyxZDmXv9wCGQgkdR2zvf7XWcOHP-_fea-RenCtrk=s96-c', ''),
(41, 'RPT MCK', 'rptmck@gmail.com', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRIgtpF7qzAlBhcsCoMr_Qbl1SGcbGpJWBvqQ&usqp=CAU', '123456'),
(42, 'Naruto', 'narutobaco@gmail.com', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRIgtpF7qzAlBhcsCoMr_Qbl1SGcbGpJWBvqQ&usqp=CAU', '123456');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `grammar`
--
ALTER TABLE `grammar`
  ADD CONSTRAINT `grammar_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `paraphrase`
--
ALTER TABLE `paraphrase`
  ADD CONSTRAINT `paraphrase_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `plagiarism`
--
ALTER TABLE `plagiarism`
  ADD CONSTRAINT `plagiarism_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `textcomplete`
--
ALTER TABLE `textcomplete`
  ADD CONSTRAINT `textcomplete_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
