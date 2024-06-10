CREATE TABLE friends(
  id INTEGER,
  name TEXT,
  birthday DATE
);

INSERT INTO friends (id, name, birthday)
VALUES (1, 'Ororo Munroe', '1940-05-30');

INSERT INTO friends (id, name, birthday)
VALUES (2, 'Borey Sep', '1985-04-20');

INSERT INTO friends (id, name, birthday)
VALUES (3, 'Ashleigh King', '1988-02-14');

SELECT * FROM friends;

UPDATE friends
SET name = 'Storm'
WHERE name = 'Ororo Munroe';

SELECT * FROM friends;

ALTER TABLE friends
ADD Email TEXT;

UPDATE friends
SET email = 'storm@codecademy.com'
WHERE id = 1;

UPDATE friends
SET email = 'boreysep@codecademy.com'
WHERE id = 2;

UPDATE friends
SET email = 'ashleighking@codecademy.com'
WHERE id = 3;

SELECT * FROM friends;

DELETE FROM friends
WHERE id = 1;

SELECT * FROM friends;