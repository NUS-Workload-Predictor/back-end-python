# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.5.5-10.1.21-MariaDB)
# Database: nusworks
# Generation Time: 2017-01-29 09:14:34 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table assignment_difficulty
# ------------------------------------------------------------

DROP TABLE IF EXISTS `assignment_difficulty`;

CREATE TABLE `assignment_difficulty` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `code` varchar(10) NOT NULL DEFAULT '',
  `time` float NOT NULL,
  `percentage` float NOT NULL,
  `coverage` float NOT NULL,
  `people` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table assignment_workload
# ------------------------------------------------------------

DROP TABLE IF EXISTS `assignment_workload`;

CREATE TABLE `assignment_workload` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `code` varchar(10) NOT NULL DEFAULT '',
  `time` float NOT NULL,
  `percentage` float NOT NULL,
  `coverage` float NOT NULL,
  `people` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table exam_difficulty
# ------------------------------------------------------------

DROP TABLE IF EXISTS `exam_difficulty`;

CREATE TABLE `exam_difficulty` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `code` varchar(10) NOT NULL DEFAULT '',
  `percentage` float NOT NULL,
  `coverage` float NOT NULL,
  `duration` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table exam_workload
# ------------------------------------------------------------

DROP TABLE IF EXISTS `exam_workload`;

CREATE TABLE `exam_workload` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `code` varchar(10) NOT NULL DEFAULT '',
  `percentage` float NOT NULL,
  `coverage` float NOT NULL,
  `duration` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table presentation_difficulty
# ------------------------------------------------------------

DROP TABLE IF EXISTS `presentation_difficulty`;

CREATE TABLE `presentation_difficulty` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `code` varchar(10) NOT NULL DEFAULT '',
  `time` float NOT NULL,
  `percentage` float NOT NULL,
  `coverage` float NOT NULL,
  `people` float NOT NULL,
  `duration` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table presentation_workload
# ------------------------------------------------------------

DROP TABLE IF EXISTS `presentation_workload`;

CREATE TABLE `presentation_workload` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `code` varchar(10) NOT NULL DEFAULT '',
  `time` float NOT NULL,
  `percentage` float NOT NULL,
  `coverage` float NOT NULL,
  `people` float NOT NULL,
  `duration` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table project_difficulty
# ------------------------------------------------------------

DROP TABLE IF EXISTS `project_difficulty`;

CREATE TABLE `project_difficulty` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `code` varchar(10) NOT NULL DEFAULT '',
  `time` float NOT NULL,
  `percentage` float NOT NULL,
  `coverage` float NOT NULL,
  `people` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table project_workload
# ------------------------------------------------------------

DROP TABLE IF EXISTS `project_workload`;

CREATE TABLE `project_workload` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `code` varchar(10) NOT NULL DEFAULT '',
  `time` float NOT NULL,
  `percentage` float NOT NULL,
  `coverage` float NOT NULL,
  `people` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table reading_difficulty
# ------------------------------------------------------------

DROP TABLE IF EXISTS `reading_difficulty`;

CREATE TABLE `reading_difficulty` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `code` varchar(10) NOT NULL DEFAULT '',
  `amount` float NOT NULL,
  `difficulty` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table reading_workload
# ------------------------------------------------------------

DROP TABLE IF EXISTS `reading_workload`;

CREATE TABLE `reading_workload` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `code` varchar(10) NOT NULL DEFAULT '',
  `amount` float NOT NULL,
  `difficulty` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table test_difficulty
# ------------------------------------------------------------

DROP TABLE IF EXISTS `test_difficulty`;

CREATE TABLE `test_difficulty` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `code` varchar(10) NOT NULL DEFAULT '',
  `percentage` float NOT NULL,
  `coverage` float NOT NULL,
  `duration` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table test_workload
# ------------------------------------------------------------

DROP TABLE IF EXISTS `test_workload`;

CREATE TABLE `test_workload` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `code` varchar(10) NOT NULL DEFAULT '',
  `percentage` float NOT NULL,
  `coverage` float NOT NULL,
  `duration` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
