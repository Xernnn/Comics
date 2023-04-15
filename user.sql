CREATE SCHEMA IF NOT EXISTS comics;
use comics;
CREATE TABLE users (
	username varchar(255),
    password varchar (255),
    avatar text,
    gmail varchar(255),
    role varchar (255),
    age int, 
    favorite varchar(255),
    PRIMARY KEY (
        username
    )
);
select * from users;
-- drop table users;

CREATE TABLE comics (
	title varchar(255),
    author varchar(255),
    artist varchar(255),
    publisher varchar(255),
    public_date date,
    genre varchar(255),
    volume int,
    series varchar(255),
    cover_image text,
    language varchar(255), 
    synopsis text,
    PRIMARY KEY (
        title
    )
);
select * from comics;
drop table comics;

CREATE TABLE sort (
	order_by varchar(255),
    PRIMARY KEY (
        order_by
    )
);
select * from sort;
-- delete from sort;
-- drop table sort;