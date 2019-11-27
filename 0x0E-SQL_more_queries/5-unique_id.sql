-- createS table with two pks
create table IF NOT EXISTS unique_id
       (id INT DEFAULT 1 UNIQUE,
       	name varchar(256));
