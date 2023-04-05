CREATE SCHEMA IF NOT EXISTS comics;
use comics;
CREATE TABLE users (
	username varchar(255),
    password varchar (255),
    priority varchar (255),
    PRIMARY KEY (
        username
    )
);
select * from users;
INSERT INTO users(username, password, priority) VALUES('tri','an','admin');
DELETE FROM users WHERE username='tri';

CREATE TABLE comics (
	title varchar(255),
    author varchar(255),
    artist varchar(255),
    publisher varchar(255),
    public_date date,
    genre varchar(1000),
    volume int,
    series varchar(255),
    cover_image varchar(255),
    language varchar(255),
    synopsis varchar(1000),
    PRIMARY KEY (
        title
    )
);
select * from comics;
drop table comics;
