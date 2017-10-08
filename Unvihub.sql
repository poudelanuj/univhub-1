ET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
drop database if exists univhub;
create database univhub;
use univhub;
SET time_zone = "+00:00";
/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
CREATE TABLE `adminprofile` (
  `id` int(11) NOT NULL,
  `consultancyName` varchar(30) NOT NULL,
  `pan_vat` varchar(20) NOT NULL,
  `reg_no` varchar(20) NOT NULL,
  `location` varchar(20) NOT NULL,
  `website` varchar(50) NOT NULL,
  `phone` int(11) NOT NULL,
  `description` longtext NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
CREATE TABLE `applytype` (
  `id` int(11) NOT NULL,
  `applytype` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
CREATE TABLE `classtype` (
  `id` int(11) NOT NULL,
  `title` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
CREATE TABLE `counselorprofile` (
  `id` int(11) NOT NULL,
  `mobile` int(11) NOT NULL,
  `address` varchar(20) NOT NULL,
  `admin_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
CREATE TABLE `country` (
  `id` int(11) NOT NULL,
  `countryname` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
CREATE TABLE `deliveryman` (
  `id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `mobile` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
INSERT INTO `deliveryman` (`id`, `name`, `mobile`) VALUES
(1, 'Hante', '1212121'),
(2, 'Paane', '56343');
CREATE TABLE `district` (
  `id` int(11) NOT NULL,
  `districtname` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
CREATE TABLE `documentfor` (
  `id` int(11) NOT NULL,
  `documentforname` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
INSERT INTO `documentfor` (`id`, `documentforname`) VALUES
(1, 'abc'),
(2, 'bcd');
CREATE TABLE `documenttype` (
  `id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
INSERT INTO `documenttype` (`id`, `name`) VALUES
(1, 'type1'),
(2, 'type2');
CREATE TABLE `header` (
  `id` int(11) NOT NULL,
  `title` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
CREATE TABLE `levels` (
  `level_id` int(11) NOT NULL,
  `level_name` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
INSERT INTO `levels` (`level_id`, `level_name`) VALUES
(1, 'Under Graduate'),
(2, 'Masters'),
(3, 'Doctorate'),
(4, 'High School');
CREATE TABLE `major` (
  `id` int(11) NOT NULL,
  `major_name` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
INSERT INTO `major` (`id`, `major_name`) VALUES
(1, 'Engineering'),
(2, 'BSC');
CREATE TABLE `moderatorprofile` (
  `id` int(11) NOT NULL,
  `mobile` int(11) NOT NULL,
  `address` varchar(20) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
CREATE TABLE `notifications` (
  `id` int(11) NOT NULL,
  `read` tinyint(1) NOT NULL,
  `title` varchar(50) DEFAULT NULL,
  `Type` int(11) DEFAULT NULL,
  `message` longtext NOT NULL,
  `created` datetime(6) NOT NULL,
  `map_url` longtext,
  `web_url` longtext,
  `receiver_id` int(11) DEFAULT NULL,
  `sender_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
CREATE TABLE `notification_type` (
  `id` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `description` varchar(400) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
CREATE TABLE `offer` (
  `id` int(11) NOT NULL,
  `title` varchar(50) NOT NULL,
  `description` longtext NOT NULL,
  `discountpercent` int(11) DEFAULT NULL,
  `scholarshippercent` int(11) DEFAULT NULL,
  `validity` date NOT NULL,
  `created` datetime(6) NOT NULL,
  `offerinclass_id` int(11) DEFAULT NULL,
  `offertype_id` int(11) NOT NULL,
  `university_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
CREATE TABLE `offeredclass` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `startdate` date NOT NULL,
  `enddate` date NOT NULL,
  `price` int(11) NOT NULL,
  `discountpercent` int(11) NOT NULL,
  `scholarshippercent` int(11) NOT NULL,
  `location` varchar(100) NOT NULL,
  `starttime` time(6) NOT NULL,
  `endtime` time(6) NOT NULL,
  `created` datetime(6) NOT NULL,
  `classtype_id` int(11) NOT NULL,
  `tutor_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
CREATE TABLE `offertype` (
  `id` int(11) NOT NULL,
  `title` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
CREATE TABLE `pickup` (
  `id` int(11) NOT NULL,
  `pickup_date` date NOT NULL,
  `time` time(6) NOT NULL,
  `location` varchar(50) NOT NULL,
  `is_pending` tinyint(1) NOT NULL,
  `created_date` date NOT NULL,
  `documentfor_id` int(11) NOT NULL,
  `pickupof_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
CREATE TABLE `pickupdetails` (
  `id` int(11) NOT NULL,
  `documentid_id` int(11) NOT NULL,
  `pickupid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
CREATE TABLE `programsoffered` (
  `id` int(11) NOT NULL,
  `programOffered` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
CREATE TABLE `ranking` (
  `u_id` int(11) DEFAULT NULL,
  `ranking` int(11) DEFAULT NULL,
  `ranking_type` enum('world','country','subject') DEFAULT NULL,
  `type_reference_table` int(11) DEFAULT NULL COMMENT 'Stores reference to the sub_major if ranking is subject ranking.'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
CREATE TABLE `registeredclass` (
  `id` int(11) NOT NULL,
  `offeredclass_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
CREATE TABLE `requirements` (
  `id` int(11) NOT NULL,
  `name` varchar(250) DEFAULT NULL,
  `description` longtext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
INSERT INTO `requirements` (`id`, `name`, `description`) VALUES
(1, 'Citizenship', 'must have citizenship or student visa'),
(2, 'Language', 'must have passed language test'),
(3, 'Recommendation', 'must have recommendation letter from professor'),
(4, 'Entrance', 'must have passed entrance');
CREATE TABLE `req_map` (
  `hash_id` int(11) NOT NULL,
  `u_id` int(11) NOT NULL,
  `level_id` int(11) NOT NULL,
  `submajor_id` int(11) DEFAULT NULL,
  `req_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
INSERT INTO `req_map` (`hash_id`, `u_id`, `level_id`, `submajor_id`, `req_id`) VALUES
(1, 1, 1, 1, 1),
(2, 1, 1, 2, 2),
(3, 1, 1, 3, 3),
(4, 1, 1, 4, 4),
(5, 1, 1, 5, 5),
(6, 2, 1, 1, 6),
(7, 2, 1, 2, 7),
(8, 2, 1, 3, 8),
(9, 2, 1, 4, 9),
(10, 2, 1, 5, 10),
(11, 3, 1, 1, 11),
(12, 3, 1, 2, 12),
(13, 3, 1, 3, 13),
(14, 3, 1, 4, 14),
(15, 3, 1, 5, 15),
(16, 4, 1, 1, 16),
(17, 4, 1, 2, 17),
(18, 4, 1, 3, 18),
(19, 4, 1, 4, 19),
(20, 4, 1, 5, 20),
(21, 5, 1, 1, 21),
(22, 5, 1, 2, 22),
(23, 5, 1, 3, 23),
(24, 5, 1, 4, 24),
(25, 5, 1, 5, 25);
CREATE TABLE `subjects` (
  `sub_id` int(11) NOT NULL,
  `name` longtext,
  `belongs_to` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
INSERT INTO `subjects` (`sub_id`, `name`, `belongs_to`) VALUES
(1, 'DBMS', 1),
(2, 'Fluid Mechanics', 2),
(3, 'Gear', 3),
(4, 'OS', 1),
(5, 'Optics', 4),
(6, 'Organix', 5);
CREATE TABLE `scheduledpickup` (
  `id` int(11) NOT NULL,
  `deliverydate` date NOT NULL,
  `deliverytime` time(6) NOT NULL,
  `is_picked` tinyint(1) DEFAULT NULL,
  `deliveryman_id` int(11) NOT NULL,
  `pickup_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
CREATE TABLE `sub_header` (
  `id` int(11) NOT NULL,
  `title` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
CREATE TABLE `sub_major` (
  `id` int(11) NOT NULL,
  `major_id` int(11) NOT NULL,
  `sub_major_name` varchar(250) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
INSERT INTO `sub_major` (`id`, `major_id`, `sub_major_name`) VALUES
(1, 1, 'Computer Engineering'),
(2, 1, 'Civil Engineering'),
(3, 1, 'Mechanical Engineering'),
(4, 2, 'Physics'),
(5, 2, 'Chemistry');
CREATE TABLE `sub_req_by_uni` (
  `r_id` int(11) NOT NULL,
  `description` longtext
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
INSERT INTO `sub_req_by_uni` (`r_id`, `description`) VALUES
(1, 'student should have GRE score more than 3.6'),
(2, 'student should have GRE score more than 3.5'),
(3, 'student should have GRE score more than 3'),
(4, 'student should have GRE score more than 2.7'),
(5, 'student should have GRE score more than 2.5'),
(6, 'student should have GRE score more than 2.6'),
(7, 'graduated from High School'),
(8, 'student studied mathematics in high school elective'),
(9, 'student should have GRE score more than 3.6'),
(10, 'student should have GRE score more than 3.4'),
(11, 'graduated from High School'),
(12, 'graduated from High School'),
(13, 'graduated from High School'),
(14, 'graduated from High School'),
(15, 'graduated from High School'),
(16, 'graduated from High School'),
(17, 'graduated from High School'),
(18, 'graduated from High School'),
(19, 'graduated from High School'),
(20, 'graduated from High School'),
(21, 'graduated from High School'),
(22, 'graduated from High School'),
(23, 'graduated from High School'),
(24, 'graduated from High School'),
(25, 'graduated from High School');
CREATE TABLE `tutor` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `qualification` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
CREATE TABLE `universities` (
  `id` int(11) NOT NULL,
  `name` varchar(250) DEFAULT NULL,
  `country` varchar(100) DEFAULT NULL,
  `logo_url` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
INSERT INTO `universities` (`id`, `name`, `country`, `logo_url`) VALUES
(1, 'MIT', 'America', 'https://i.imgur.com/6loFlvn.jpg'),
(2, 'Harvard', 'America', 'https://i.imgur.com/6loFlvn.jpg'),
(3, 'Howard', 'America', 'https://i.imgur.com/UP0iUP1.jpg'),
(4, 'Arkansas', 'America', 'https://i.imgur.com/UP0iUP1.jpg'),
(5, 'Stanford', 'America', 'https://i.imgur.com/UP0iUP1.jpg');
CREATE TABLE `university_content` (
  `id` int(11) NOT NULL,
  `u_id` int(11) NOT NULL,
  `h_id` int(11) NOT NULL,
  `sh_id` int(11) DEFAULT NULL,
  `description` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
CREATE TABLE `university_requirement` (
  `u_id` int(11) NOT NULL,
  `r_id` int(11) NOT NULL,
  `base_score` int(11) DEFAULT NULL	
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
CREATE TABLE `uni_address` (
  `id` int(11) NOT NULL,
  `country` varchar(100) NOT NULL,
  `state` varchar(100) NOT NULL,
  `city` varchar(250) NOT NULL,
  `street` varchar(250) DEFAULT NULL,
  `zip_code` smallint(5) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
INSERT INTO `uni_address` (`id`, `country`, `state`, `city`, `street`, `zip_code`) VALUES
(1, 'America', 'Massachusetts', 'Cambridge', 'MIT Street', 4400),
(2, 'America', 'Massachusetts', 'Cambridge', 'Harvard Street', 2220),
(3, 'America', 'California', 'XYZ', 'Howard Street', 2220),
(4, 'America', 'San Franscisco', 'XYZ', 'Arkansas Street', 2220),
(5, 'America', 'Michigan', 'XYZ', 'Stranford Street', 2320);
CREATE TABLE `uni_address_mapping` (
  `u_id` int(11) DEFAULT NULL,
  `a_id` int(11) DEFAULT NULL,
  `is_main` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
INSERT INTO `uni_address_mapping` (`u_id`, `a_id`, `is_main`) VALUES
(1, 1, 1),
(2, 2, 1),
(3, 3, 1),
(4, 4, 1),
(5, 5, 1);
CREATE TABLE `uploadeddocuments` (
  `id` int(11) NOT NULL,
  `docname` varchar(30) NOT NULL,
  `url` longtext NOT NULL,
  `doctype_id` int(11) NOT NULL,
  `student_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
INSERT INTO `uploadeddocuments` (`id`, `docname`, `url`, `doctype_id`, `student_id_id`) VALUES
(1, 'doc1of1', 'adadad', 1, 2),
(2, 'doc2of1', 'afsaf', 2, 2),
(3, 'doc1of2', 'dfgseeg', 1, 3),
(4, 'doc1of3', 'sgsg', 1, 4),
(5, 'doc2of2', 'sdhfg', 2, 4);
CREATE TABLE `user_profile` (
  `id` int(11) NOT NULL,
  `dob` date NOT NULL,
  `mobile` int(11) NOT NULL,
  `remember_token` varchar(100) DEFAULT NULL,
  `updated_at` datetime(6) DEFAULT NULL,
  `scholarship` tinyint(1) NOT NULL,
  `citizenship` varchar(15) NOT NULL,
  `passport` varchar(15) DEFAULT NULL,
  `apply_for_id` int(11) NOT NULL,
  `apply_type_id` int(11) NOT NULL,
  `district_id` int(11) NOT NULL,
  `program_id` int(11) NOT NULL,
  `sub_major_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
ALTER TABLE `adminprofile`
  ADD PRIMARY KEY (`id`),
  ADD KEY `adminprofile_user_id_0bfbb423_fk_auth_user_id` (`user_id`);
ALTER TABLE `applytype`
  ADD PRIMARY KEY (`id`);
ALTER TABLE `classtype`
  ADD PRIMARY KEY (`id`);
ALTER TABLE `counselorprofile`
  ADD PRIMARY KEY (`id`),
  ADD KEY `counselorprofile_admin_id_3a37237e_fk_auth_user_id` (`admin_id`),
  ADD KEY `counselorprofile_user_id_4f399045_fk_auth_user_id` (`user_id`);
ALTER TABLE `country`
  ADD PRIMARY KEY (`id`);
ALTER TABLE `deliveryman`
  ADD PRIMARY KEY (`id`);
ALTER TABLE `district`
  ADD PRIMARY KEY (`id`);
ALTER TABLE `documentfor`
  ADD PRIMARY KEY (`id`);
ALTER TABLE `documenttype`
  ADD PRIMARY KEY (`id`);
ALTER TABLE `header`
  ADD PRIMARY KEY (`id`);
ALTER TABLE `levels`
  ADD PRIMARY KEY (`level_id`);
ALTER TABLE `major`
  ADD PRIMARY KEY (`id`);
ALTER TABLE `moderatorprofile`
  ADD PRIMARY KEY (`id`),
  ADD KEY `moderatorprofile_user_id_828c1e8f_fk_auth_user_id` (`user_id`);
ALTER TABLE `notifications`
  ADD PRIMARY KEY (`id`),
  ADD KEY `notifications_receiver_id_b708b2b0_fk_auth_user_id` (`receiver_id`),
  ADD KEY `notifications_sender_id_57e62d28_fk_auth_user_id` (`sender_id`);
ALTER TABLE `notification_type`
  ADD PRIMARY KEY (`id`);
ALTER TABLE `offer`
  ADD PRIMARY KEY (`id`),
  ADD KEY `offer_offerinclass_id_2f103e92_fk_offeredclass_id` (`offerinclass_id`),
  ADD KEY `offer_offertype_id_5546cc7d_fk_offertype_id` (`offertype_id`),
  ADD KEY `offer_university_id_44a39177_fk_universities_id` (`university_id`);
ALTER TABLE `offeredclass`
  ADD PRIMARY KEY (`id`),
  ADD KEY `offeredclass_classtype_id_a823c4f8_fk_classtype_id` (`classtype_id`),
  ADD KEY `offeredclass_tutor_id_4a15a2db_fk_tutor_id` (`tutor_id`);
ALTER TABLE `offertype`
  ADD PRIMARY KEY (`id`);
ALTER TABLE `pickup`
  ADD PRIMARY KEY (`id`),
  ADD KEY `pickup_documentfor_id_3b65d8fb_fk_documentfor_id` (`documentfor_id`),
  ADD KEY `pickup_pickupof_id_349bcaf2_fk_auth_user_id` (`pickupof_id`);
ALTER TABLE `pickupdetails`
  ADD PRIMARY KEY (`id`),
  ADD KEY `pickupdetails_documentid_id_5757fbf4_fk_uploadeddocuments_id` (`documentid_id`),
  ADD KEY `pickupdetails_pickupid_id_6c59a357_fk_pickup_id` (`pickupid_id`);
ALTER TABLE `programsoffered`
  ADD PRIMARY KEY (`id`);
ALTER TABLE `ranking`
  ADD KEY `fk_ranking_1_idx` (`u_id`);
ALTER TABLE `registeredclass`
  ADD PRIMARY KEY (`id`),
  ADD KEY `registeredclass_offeredclass_id_e7df6999_fk_offeredclass_id` (`offeredclass_id`),
  ADD KEY `registeredclass_user_id_52cbf9af_fk_auth_user_id` (`user_id`);
ALTER TABLE `requirements`
  ADD PRIMARY KEY (`id`);
ALTER TABLE `req_map`
  ADD PRIMARY KEY (`hash_id`),
  ADD KEY `foreign_key_u_id_idx` (`u_id`),
  ADD KEY `foreign_key_level_id_idx` (`level_id`),
  ADD KEY `f_req_idx` (`req_id`),
  ADD KEY `fk_submajor` (`submajor_id`);
ALTER TABLE `subjects`
  ADD PRIMARY KEY (`sub_id`),
  ADD KEY `belongs to submajor_idx` (`belongs_to`);
ALTER TABLE `scheduledpickup`
  ADD PRIMARY KEY (`id`),
  ADD KEY `scheduledpickup_deliveryman_id_9ba8a2a4_fk_deliveryman_id` (`deliveryman_id`),
  ADD KEY `scheduledpickup_pickup_id_b3db2b8c_fk_pickup_id` (`pickup_id`);
ALTER TABLE `sub_header`
  ADD PRIMARY KEY (`id`);
ALTER TABLE `sub_major`
  ADD PRIMARY KEY (`id`),
  ADD KEY `major_id` (`major_id`);
ALTER TABLE `sub_req_by_uni`
  ADD PRIMARY KEY (`r_id`);
ALTER TABLE `tutor`
  ADD PRIMARY KEY (`id`);
ALTER TABLE `universities`
  ADD PRIMARY KEY (`id`);
ALTER TABLE `university_content`
  ADD PRIMARY KEY (`id`),
  ADD KEY `u_id` (`u_id`),
  ADD KEY `h_id` (`h_id`),
  ADD KEY `sh_id` (`sh_id`);
ALTER TABLE `university_requirement`
  ADD KEY `u_id` (`u_id`),
  ADD KEY `r_id` (`r_id`);
ALTER TABLE `uni_address`
  ADD PRIMARY KEY (`id`);
ALTER TABLE `uni_address_mapping`
  ADD KEY `fk_uni_address_mapping_1_idx` (`a_id`),
  ADD KEY `fk_uni_address_mapping_2_idx` (`u_id`);
ALTER TABLE `uploadeddocuments`
  ADD PRIMARY KEY (`id`),
  ADD KEY `uploadeddocuments_doctype_id_197173dc_fk_documenttype_id` (`doctype_id`),
  ADD KEY `uploadeddocuments_student_id_id_d8b8874c_fk_auth_user_id` (`student_id_id`);
ALTER TABLE `user_profile`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`),
  ADD KEY `user_profile_apply_for_id_c5ade08d_fk_country_id` (`apply_for_id`),
  ADD KEY `user_profile_apply_type_id_5a2ccf54_fk_applytype_id` (`apply_type_id`),
  ADD KEY `user_profile_district_id_f5a3a176_fk_district_id` (`district_id`),
  ADD KEY `user_profile_program_id_599a58a5_fk_programsOffered_id` (`program_id`),
  ADD KEY `user_profile_sub_major_id_15e239a7_fk_sub_major_id` (`sub_major_id`);
ALTER TABLE `adminprofile`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE `applytype`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE `classtype`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE `counselorprofile`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE `country`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE `deliveryman`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
ALTER TABLE `district`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE `documentfor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
ALTER TABLE `documenttype`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
ALTER TABLE `header`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE `major`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE `moderatorprofile`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE `notifications`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE `offer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE `offeredclass`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE `offertype`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE `pickup`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
ALTER TABLE `pickupdetails`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
ALTER TABLE `programsoffered`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE `ranking`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE `registeredclass`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE `requirements`
  MODIFY `u_id` int(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE `scheduledpickup`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
ALTER TABLE `sub_header`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE `sub_major`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE `tutor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE `universities`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE `university_content`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE `university_requirement`
  MODIFY `u_id` int(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE `uni_address`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE `uni_address_mapping`
  MODIFY `u_id` int(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE `uploadeddocuments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
ALTER TABLE `user_profile`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE `counselorprofile`
  ADD CONSTRAINT `counselorprofile_admin_id_3a37237e_fk_auth_user_id` FOREIGN KEY (`admin_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `counselorprofile_user_id_4f399045_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
ALTER TABLE `moderatorprofile`
  ADD CONSTRAINT `moderatorprofile_user_id_828c1e8f_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
ALTER TABLE `notifications`
  ADD CONSTRAINT `notifications_receiver_id_b708b2b0_fk_auth_user_id` FOREIGN KEY (`receiver_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `notifications_sender_id_57e62d28_fk_auth_user_id` FOREIGN KEY (`sender_id`) REFERENCES `auth_user` (`id`);
ALTER TABLE `offer`
  ADD CONSTRAINT `offer_offerinclass_id_2f103e92_fk_offeredclass_id` FOREIGN KEY (`offerinclass_id`) REFERENCES `offeredclass` (`id`),
  ADD CONSTRAINT `offer_offertype_id_5546cc7d_fk_offertype_id` FOREIGN KEY (`offertype_id`) REFERENCES `offertype` (`id`),
  ADD CONSTRAINT `offer_university_id_44a39177_fk_universities_id` FOREIGN KEY (`university_id`) REFERENCES `universities` (`id`);
ALTER TABLE `offeredclass`
  ADD CONSTRAINT `offeredclass_classtype_id_a823c4f8_fk_classtype_id` FOREIGN KEY (`classtype_id`) REFERENCES `classtype` (`id`),
  ADD CONSTRAINT `offeredclass_tutor_id_4a15a2db_fk_tutor_id` FOREIGN KEY (`tutor_id`) REFERENCES `tutor` (`id`);
ALTER TABLE `pickup`
  ADD CONSTRAINT `pickup_documentfor_id_3b65d8fb_fk_documentfor_id` FOREIGN KEY (`documentfor_id`) REFERENCES `documentfor` (`id`),
  ADD CONSTRAINT `pickup_pickupof_id_349bcaf2_fk_auth_user_id` FOREIGN KEY (`pickupof_id`) REFERENCES `auth_user` (`id`);
ALTER TABLE `pickupdetails`
  ADD CONSTRAINT `pickupdetails_documentid_id_5757fbf4_fk_uploadeddocuments_id` FOREIGN KEY (`documentid_id`) REFERENCES `uploadeddocuments` (`id`),
  ADD CONSTRAINT `pickupdetails_pickupid_id_6c59a357_fk_pickup_id` FOREIGN KEY (`pickupid_id`) REFERENCES `pickup` (`id`);
ALTER TABLE `ranking`
  ADD CONSTRAINT `fk_ranking__1` FOREIGN KEY (`u_id`) REFERENCES `universities` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE `req_map`
  ADD CONSTRAINT `f_req` FOREIGN KEY (`req_id`) REFERENCES `sub_req_by_uni` (`r_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_submajor` FOREIGN KEY (`submajor_id`) REFERENCES `sub_major` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `foreign_key_level_id` FOREIGN KEY (`level_id`) REFERENCES `levels` (`level_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `foreign_key_u_id` FOREIGN KEY (`u_id`) REFERENCES `universities` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE `subjects`
  ADD CONSTRAINT `sub_to_submajor` FOREIGN KEY (`belongs_to`) REFERENCES `sub_major` (`id`);
ALTER TABLE `registeredclass`
  ADD CONSTRAINT `registeredclass_offeredclass_id_e7df6999_fk_offeredclass_id` FOREIGN KEY (`offeredclass_id`) REFERENCES `offeredclass` (`id`),
  ADD CONSTRAINT `registeredclass_user_id_52cbf9af_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
ALTER TABLE `scheduledpickup`
  ADD CONSTRAINT `scheduledpickup_deliveryman_id_9ba8a2a4_fk_deliveryman_id` FOREIGN KEY (`deliveryman_id`) REFERENCES `deliveryman` (`id`),
  ADD CONSTRAINT `scheduledpickup_pickup_id_b3db2b8c_fk_pickup_id` FOREIGN KEY (`pickup_id`) REFERENCES `pickup` (`id`);
ALTER TABLE `sub_major`
  ADD CONSTRAINT `fk_sub_major__1` FOREIGN KEY (`major_id`) REFERENCES `major` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE `university_content`
  ADD CONSTRAINT `fk_university_content_1` FOREIGN KEY (`u_id`) REFERENCES `universities` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_university_content_2` FOREIGN KEY (`h_id`) REFERENCES `header` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_university_content_3` FOREIGN KEY (`sh_id`) REFERENCES `sub_header` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE `university_requirement`
  ADD CONSTRAINT `fk_university_requirement_1` FOREIGN KEY (`u_id`) REFERENCES `universities` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_university_requirement_2` FOREIGN KEY (`r_id`) REFERENCES `requirements` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE `uni_address_mapping`
  ADD CONSTRAINT `fk_uni_address_mapping_1` FOREIGN KEY (`a_id`) REFERENCES `uni_address` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_uni_address_mapping_2` FOREIGN KEY (`u_id`) REFERENCES `universities` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE `uploadeddocuments`	
  ADD CONSTRAINT `uploadeddocuments_doctype_id_197173dc_fk_documenttype_id` FOREIGN KEY (`doctype_id`) REFERENCES `documenttype` (`id`),
  ADD CONSTRAINT `uploadeddocuments_student_id_id_d8b8874c_fk_auth_user_id` FOREIGN KEY (`student_id_id`) REFERENCES `auth_user` (`id`);
ALTER TABLE `user_profile`
  ADD CONSTRAINT `user_profile_apply_for_id_c5ade08d_fk_country_id` FOREIGN KEY (`apply_for_id`) REFERENCES `country` (`id`),
  ADD CONSTRAINT `user_profile_apply_type_id_5a2ccf54_fk_applytype_id` FOREIGN KEY (`apply_type_id`) REFERENCES `applytype` (`id`),
  ADD CONSTRAINT `user_profile_district_id_f5a3a176_fk_district_id` FOREIGN KEY (`district_id`) REFERENCES `district` (`id`),
  ADD CONSTRAINT `user_profile_program_id_599a58a5_fk_programsOffered_id` FOREIGN KEY (`program_id`) REFERENCES `programsoffered` (`id`),
  ADD CONSTRAINT `user_profile_sub_major_id_15e239a7_fk_sub_major_id` FOREIGN KEY (`sub_major_id`) REFERENCES `sub_major` (`id`),
  ADD CONSTRAINT `user_profile_user_id_8fdce8e2_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

