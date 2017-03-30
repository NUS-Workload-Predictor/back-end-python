# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.5.5-10.1.21-MariaDB)
# Database: nusworks
# Generation Time: 2017-03-30 12:16:43 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table assignment_workload_complex
# ------------------------------------------------------------

DROP TABLE IF EXISTS `assignment_workload_complex`;

CREATE TABLE `assignment_workload_complex` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(10) DEFAULT NULL,
  `cap` float DEFAULT NULL,
  `semesters` float DEFAULT NULL,
  `credits` float DEFAULT NULL,
  `time` float DEFAULT NULL,
  `percentage` float DEFAULT NULL,
  `coverage` float DEFAULT NULL,
  `people` float DEFAULT NULL,
  `intercept` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table assignment_workload_complex_data
# ------------------------------------------------------------

DROP TABLE IF EXISTS `assignment_workload_complex_data`;

CREATE TABLE `assignment_workload_complex_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(10) DEFAULT NULL,
  `cap` float DEFAULT NULL,
  `semesters` float DEFAULT NULL,
  `credits` float DEFAULT NULL,
  `time` float DEFAULT NULL,
  `percentage` float DEFAULT NULL,
  `coverage` float DEFAULT NULL,
  `people` float DEFAULT NULL,
  `result` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table assignment_workload_simple
# ------------------------------------------------------------

DROP TABLE IF EXISTS `assignment_workload_simple`;

CREATE TABLE `assignment_workload_simple` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(10) DEFAULT NULL,
  `time` float DEFAULT NULL,
  `percentage` float DEFAULT NULL,
  `coverage` float DEFAULT NULL,
  `people` float DEFAULT NULL,
  `intercept` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table assignment_workload_simple_data
# ------------------------------------------------------------

DROP TABLE IF EXISTS `assignment_workload_simple_data`;

CREATE TABLE `assignment_workload_simple_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(10) DEFAULT NULL,
  `time` float DEFAULT NULL,
  `percentage` float DEFAULT NULL,
  `coverage` float DEFAULT NULL,
  `people` float DEFAULT NULL,
  `result` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table difficulty_complex
# ------------------------------------------------------------

DROP TABLE IF EXISTS `difficulty_complex`;

CREATE TABLE `difficulty_complex` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(10) DEFAULT NULL,
  `cap` float DEFAULT NULL,
  `semesters` float DEFAULT NULL,
  `credits` float DEFAULT NULL,
  `level` float DEFAULT NULL,
  `mc` float DEFAULT NULL,
  `lecture` float DEFAULT NULL,
  `tutorial` float DEFAULT NULL,
  `lab` float DEFAULT NULL,
  `project` float DEFAULT NULL,
  `preparation` float DEFAULT NULL,
  `intercept` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table difficulty_complex_data
# ------------------------------------------------------------

DROP TABLE IF EXISTS `difficulty_complex_data`;

CREATE TABLE `difficulty_complex_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(10) DEFAULT NULL,
  `cap` float DEFAULT NULL,
  `semesters` float DEFAULT NULL,
  `credits` float DEFAULT NULL,
  `level` float DEFAULT NULL,
  `mc` float DEFAULT NULL,
  `lecture` float DEFAULT NULL,
  `tutorial` float DEFAULT NULL,
  `lab` float DEFAULT NULL,
  `project` float DEFAULT NULL,
  `preparation` float DEFAULT NULL,
  `result` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table difficulty_simple
# ------------------------------------------------------------

DROP TABLE IF EXISTS `difficulty_simple`;

CREATE TABLE `difficulty_simple` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(10) DEFAULT NULL,
  `level` float DEFAULT NULL,
  `mc` float DEFAULT NULL,
  `lecture` float DEFAULT NULL,
  `tutorial` float DEFAULT NULL,
  `lab` float DEFAULT NULL,
  `project` float DEFAULT NULL,
  `preparation` float DEFAULT NULL,
  `intercept` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table difficulty_simple_data
# ------------------------------------------------------------

DROP TABLE IF EXISTS `difficulty_simple_data`;

CREATE TABLE `difficulty_simple_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(10) DEFAULT NULL,
  `level` float DEFAULT NULL,
  `mc` float DEFAULT NULL,
  `lecture` float DEFAULT NULL,
  `tutorial` float DEFAULT NULL,
  `lab` float DEFAULT NULL,
  `project` float DEFAULT NULL,
  `preparation` float DEFAULT NULL,
  `result` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table exam_workload_complex
# ------------------------------------------------------------

DROP TABLE IF EXISTS `exam_workload_complex`;

CREATE TABLE `exam_workload_complex` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(10) DEFAULT NULL,
  `cap` float DEFAULT NULL,
  `semesters` float DEFAULT NULL,
  `credits` float DEFAULT NULL,
  `percentage` float DEFAULT NULL,
  `coverage` float DEFAULT NULL,
  `duration` float DEFAULT NULL,
  `intercept` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table exam_workload_complex_data
# ------------------------------------------------------------

DROP TABLE IF EXISTS `exam_workload_complex_data`;

CREATE TABLE `exam_workload_complex_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(10) DEFAULT NULL,
  `cap` float DEFAULT NULL,
  `semesters` float DEFAULT NULL,
  `credits` float DEFAULT NULL,
  `percentage` float DEFAULT NULL,
  `coverage` float DEFAULT NULL,
  `duration` float DEFAULT NULL,
  `result` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table exam_workload_simple
# ------------------------------------------------------------

DROP TABLE IF EXISTS `exam_workload_simple`;

CREATE TABLE `exam_workload_simple` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(10) DEFAULT NULL,
  `percentage` float DEFAULT NULL,
  `coverage` float DEFAULT NULL,
  `duration` float DEFAULT NULL,
  `intercept` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table exam_workload_simple_data
# ------------------------------------------------------------

DROP TABLE IF EXISTS `exam_workload_simple_data`;

CREATE TABLE `exam_workload_simple_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(10) DEFAULT NULL,
  `percentage` float DEFAULT NULL,
  `coverage` float DEFAULT NULL,
  `duration` float DEFAULT NULL,
  `result` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table presentation_workload_complex
# ------------------------------------------------------------

DROP TABLE IF EXISTS `presentation_workload_complex`;

CREATE TABLE `presentation_workload_complex` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(10) DEFAULT NULL,
  `time` float DEFAULT NULL,
  `percentage` float DEFAULT NULL,
  `coverage` float DEFAULT NULL,
  `people` float DEFAULT NULL,
  `intercept` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table presentation_workload_complex_data
# ------------------------------------------------------------

DROP TABLE IF EXISTS `presentation_workload_complex_data`;

CREATE TABLE `presentation_workload_complex_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(10) DEFAULT NULL,
  `cap` float DEFAULT NULL,
  `semesters` float DEFAULT NULL,
  `credits` float DEFAULT NULL,
  `time` float DEFAULT NULL,
  `percentage` float DEFAULT NULL,
  `coverage` float DEFAULT NULL,
  `people` float DEFAULT NULL,
  `duration` float DEFAULT NULL,
  `result` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table presentation_workload_simple
# ------------------------------------------------------------

DROP TABLE IF EXISTS `presentation_workload_simple`;

CREATE TABLE `presentation_workload_simple` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(10) DEFAULT NULL,
  `time` float DEFAULT NULL,
  `percentage` float DEFAULT NULL,
  `coverage` float DEFAULT NULL,
  `people` float DEFAULT NULL,
  `intercept` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table presentation_workload_simple_data
# ------------------------------------------------------------

DROP TABLE IF EXISTS `presentation_workload_simple_data`;

CREATE TABLE `presentation_workload_simple_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(10) DEFAULT NULL,
  `time` float DEFAULT NULL,
  `percentage` float DEFAULT NULL,
  `coverage` float DEFAULT NULL,
  `people` float DEFAULT NULL,
  `duration` float DEFAULT NULL,
  `result` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table project_workload_complex
# ------------------------------------------------------------

DROP TABLE IF EXISTS `project_workload_complex`;

CREATE TABLE `project_workload_complex` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(10) DEFAULT NULL,
  `time` float DEFAULT NULL,
  `percentage` float DEFAULT NULL,
  `coverage` float DEFAULT NULL,
  `people` float DEFAULT NULL,
  `intercept` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table project_workload_complex_data
# ------------------------------------------------------------

DROP TABLE IF EXISTS `project_workload_complex_data`;

CREATE TABLE `project_workload_complex_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(10) DEFAULT NULL,
  `cap` float DEFAULT NULL,
  `semesters` float DEFAULT NULL,
  `credits` float DEFAULT NULL,
  `time` float DEFAULT NULL,
  `percentage` float DEFAULT NULL,
  `coverage` float DEFAULT NULL,
  `people` float DEFAULT NULL,
  `result` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table project_workload_simple
# ------------------------------------------------------------

DROP TABLE IF EXISTS `project_workload_simple`;

CREATE TABLE `project_workload_simple` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(10) DEFAULT NULL,
  `time` float DEFAULT NULL,
  `percentage` float DEFAULT NULL,
  `coverage` float DEFAULT NULL,
  `people` float DEFAULT NULL,
  `intercept` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table project_workload_simple_data
# ------------------------------------------------------------

DROP TABLE IF EXISTS `project_workload_simple_data`;

CREATE TABLE `project_workload_simple_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(10) DEFAULT NULL,
  `time` float DEFAULT NULL,
  `percentage` float DEFAULT NULL,
  `coverage` float DEFAULT NULL,
  `people` float DEFAULT NULL,
  `result` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table reading_workload_complex
# ------------------------------------------------------------

DROP TABLE IF EXISTS `reading_workload_complex`;

CREATE TABLE `reading_workload_complex` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(10) DEFAULT NULL,
  `cap` float DEFAULT NULL,
  `semesters` float DEFAULT NULL,
  `credits` float DEFAULT NULL,
  `amount` float DEFAULT NULL,
  `intercept` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table reading_workload_complex_data
# ------------------------------------------------------------

DROP TABLE IF EXISTS `reading_workload_complex_data`;

CREATE TABLE `reading_workload_complex_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(10) DEFAULT NULL,
  `cap` float DEFAULT NULL,
  `semesters` float DEFAULT NULL,
  `credits` float DEFAULT NULL,
  `amount` float DEFAULT NULL,
  `result` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table reading_workload_simple
# ------------------------------------------------------------

DROP TABLE IF EXISTS `reading_workload_simple`;

CREATE TABLE `reading_workload_simple` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(10) DEFAULT NULL,
  `amount` float DEFAULT NULL,
  `intercept` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table reading_workload_simple_data
# ------------------------------------------------------------

DROP TABLE IF EXISTS `reading_workload_simple_data`;

CREATE TABLE `reading_workload_simple_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(10) DEFAULT NULL,
  `amount` float DEFAULT NULL,
  `result` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table simple_module_difficulty
# ------------------------------------------------------------

DROP TABLE IF EXISTS `simple_module_difficulty`;

CREATE TABLE `simple_module_difficulty` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `code` varchar(10) NOT NULL DEFAULT '',
  `level` float NOT NULL,
  `lecture` float NOT NULL,
  `tutorial` float NOT NULL,
  `lab` float NOT NULL,
  `project` float NOT NULL,
  `preparation` float NOT NULL,
  `intercept` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table simple_module_difficulty_data
# ------------------------------------------------------------

DROP TABLE IF EXISTS `simple_module_difficulty_data`;

CREATE TABLE `simple_module_difficulty_data` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `code` varchar(10) NOT NULL DEFAULT '',
  `level` float NOT NULL,
  `lecture` float NOT NULL,
  `tutorial` float NOT NULL,
  `lab` float NOT NULL,
  `project` float NOT NULL,
  `preparation` float NOT NULL,
  `result` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table test_workload_complex
# ------------------------------------------------------------

DROP TABLE IF EXISTS `test_workload_complex`;

CREATE TABLE `test_workload_complex` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(10) DEFAULT NULL,
  `cap` float DEFAULT NULL,
  `semesters` float DEFAULT NULL,
  `credits` float DEFAULT NULL,
  `percentage` float DEFAULT NULL,
  `coverage` float DEFAULT NULL,
  `duration` float DEFAULT NULL,
  `intercept` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table test_workload_complex_data
# ------------------------------------------------------------

DROP TABLE IF EXISTS `test_workload_complex_data`;

CREATE TABLE `test_workload_complex_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(10) DEFAULT NULL,
  `cap` float DEFAULT NULL,
  `semesters` float DEFAULT NULL,
  `credits` float DEFAULT NULL,
  `percentage` float DEFAULT NULL,
  `coverage` float DEFAULT NULL,
  `duration` float DEFAULT NULL,
  `result` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table test_workload_simple
# ------------------------------------------------------------

DROP TABLE IF EXISTS `test_workload_simple`;

CREATE TABLE `test_workload_simple` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(10) DEFAULT NULL,
  `percentage` float DEFAULT NULL,
  `coverage` float DEFAULT NULL,
  `duration` float DEFAULT NULL,
  `intercept` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table test_workload_simple_data
# ------------------------------------------------------------

DROP TABLE IF EXISTS `test_workload_simple_data`;

CREATE TABLE `test_workload_simple_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(10) DEFAULT NULL,
  `percentage` float DEFAULT NULL,
  `coverage` float DEFAULT NULL,
  `duration` float DEFAULT NULL,
  `result` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
