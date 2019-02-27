create databasee datad_demo;

use datad_demo;

DROP TABLE IF EXISTS customer;
DROP TABLE IF EXISTS customer_details;

CREATE TABLE datad_demo.customer_details(
school_name varchar(50),
official_email_address varchar(50),
contact_number varchar(50) ,
admission_info varchar(50),
school_syllabus varchar(50),
Classes_you_offer varchar(50),
school_timing varchar(50) ,
school_fee_info varchar(50),
transportation_details varchar(50),
alternate_number varchar(50),
school_working_hours varchar(50),
school_calendar varchar(50),
your_web_site_url varchar(50),
your_web_site_cloud_onprimise varchar(50),
your_web_site_allows_plugin varchar(50)
);


INSERT INTO datad_demo.customer_details VALUES(
"school1",
"school@123.com",
"47934934838",
"admission over",
"i dnot know",
"dance , zumba",
"9-4",
"323323",
"bus",
"6789",
"8",
"jan-dec",
"www.school1.com",
"no",
"yes"
);


CREATE TABLE datad_demo.others_customer_questions(
customer_name varchar(50),
question varchar(50),
answer varchar(50)
);