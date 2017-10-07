# insertions
insert ignore into header(id,title) values
(1,"About"),
(2,"Scholorship"),
(3,"Admission"),
(4,"Campuses"),
(5,"Research");

insert ignore into sub_header(id,title) values
(1,"Motto"),
(2,"Why Study"),
(3,"Features");


drop view if exists university_basic_info;
create  view  university_basic_info as
    select
        universities.`name`,
        universities.`country`,
        universities.logo_url,
        sub_header.title,
        university_content.description
        from
            universities natural join
            university_content natural join
            header  natural join
            sub_header natural join
            uni_address natural join
            uni_address_mapping
            where
                uni_address_mapping.is_main
                and header.title=1
                and (sub_header.title=1
                or sub_header.title=2);

drop view if exists university_major_sub_major_list;
create view university_major_sub_major_list as
	select
		major.major_name as major,
		sub_major.sub_major_name as sub_major
		from major natural join sub_major natural join req_map;


INSERT INTO `universities` (`id`, `name`, `country`, `logo_url`) VALUES ('1', 'MIT', 'USA', 'http://logo.png');
INSERT INTO `universities` (`id`, `name`, `country`, `logo_url`) VALUES ('2', 'Harvard', 'Uk', 'http://harvard_logo_url.png');
INSERT INTO `universities` (`id`, `name`, `country`, `logo_url`) VALUES ('3', 'American good University', 'USA', 'http://test.goodthing.jpg');


INSERT INTO `major` (`id`, `major_name`) VALUES ('1', 'Engineering');
INSERT INTO `major` (`id`, `major_name`) VALUES ('2', 'Sociology');
INSERT INTO `major` (`id`, `major_name`) VALUES ('3', 'Mathematics');

INSERT INTO `sub_major` (`id`, `sub_major_name`, `major_id`) VALUES ('1', 'Computer Engineering', '1');
INSERT INTO `sub_major` (`id`, `sub_major_name`, `major_id`) VALUES ('2', 'Electronics And Communication Engineering', '1');
INSERT INTO `sub_major` (`id`, `sub_major_name`, `major_id`) VALUES ('3', 'Electrical Engineering', '1');
INSERT INTO `sub_major` (`id`, `sub_major_name`, `major_id`) VALUES ('4', 'Statistics', '3');
INSERT INTO `sub_major` (`id`, `sub_major_name`, `major_id`) VALUES ('5', 'Algebra', '3');


INSERT INTO `univhub`.`levels` (`level_id`, `level_name`) VALUES ('1', 'Bachelor');
INSERT INTO `univhub`.`levels` (`level_id`, `level_name`) VALUES ('2', 'Masters');
INSERT INTO `univhub`.`levels` (`level_id`, `level_name`) VALUES ('3', 'Post Doc.');

INSERT INTO `univhub`.`sub_req_by_uni` (`r_id`, `description`) VALUES ('1', 'Very Important description');

INSERT INTO `univhub`.`requirements` (`id`, `name`, `description`) VALUES ('1', 'IELTS', 'the IELTS');
INSERT INTO `univhub`.`requirements` (`id`, `name`, `description`) VALUES ('2', 'GRE', 'the GRE score is required.');

INSERT INTO `univhub`.`req_map` (`hash_id`, `level_id`, `req_id`, `submajor_id`, `u_id`) VALUES ('1', '1', '1', '1', '1');
INSERT INTO `univhub`.`req_map` (`hash_id`, `level_id`, `req_id`, `submajor_id`, `u_id`) VALUES ('2', '1', '1', '2', '1');
INSERT INTO `univhub`.`req_map` (`hash_id`, `level_id`, `req_id`, `submajor_id`, `u_id`) VALUES ('3', '1', '1', '5', '1');
INSERT INTO `univhub`.`req_map` (`hash_id`, `level_id`, `req_id`, `submajor_id`, `u_id`) VALUES ('4', '1', '1', '5', '2');
