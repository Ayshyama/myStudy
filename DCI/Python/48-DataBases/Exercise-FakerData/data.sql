
DROP TABLE IF EXISTS user;
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50),
    email VARCHAR(50),
    birthdate DATE,
    country VARCHAR(50)
);
INSERT INTO user (username, email, birthdate, country) VALUES
("Natalie Holland", "dixonashley@example.com", "2015-05-19", "Mozambique"),
("Melody Cisneros", "reyescindy@example.com", "2023-07-13", "Cocos (Keeling) Islands"),
("Nicholas Padilla", "gary10@example.org", "2017-12-16", "Svalbard & Jan Mayen Islands"),
("Scott Jones", "wbeck@example.org", "1981-09-01", "Malaysia"),
("Andrew Green", "vanessagomez@example.org", "2021-05-23", "Hong Kong");