
CREATE TABLE taxis (
    id INTEGER PRIMARY KEY,
    driver_name TEXT NOT NULL,
    car_type TEXT NOT NULL
);

INSERT INTO taxis (id, driver_name, car_type) VALUES
(1, 'Moshe Levi', 'Van'),
(2, 'Rina Cohen', 'Sedan'),
(3, 'David Azulay', 'Minibus'),
(4, 'Maya Bar', 'Electric'),
(5, 'Yossi Peretz', 'SUV');

CREATE TABLE passengers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    destination TEXT,
    taxi_id INTEGER,
    FOREIGN KEY(taxi_id) REFERENCES taxis(id)
);

INSERT INTO passengers (id, name, destination, taxi_id) VALUES
(1, 'Tamar', 'Jerusalem', 1),
(2, 'Eitan', 'Haifa', 2),
(3, 'Noa', 'Tel Aviv', NULL),
(4, 'Lior', 'Eilat', 1),
(5, 'Dana', 'Beer Sheva', NULL),
(6, 'Gil', 'Ashdod', 3),
(7, 'Moran', 'Netanya', NULL);

SELECT passengers.* , taxis.driver_name , taxis.car_type FROM passengers 
JOIN taxis ON passengers.taxi_id = taxis.id;

SELECT p.*, t.driver_name , t.car_type FROM passengers p  
LEFT join taxis t ON p.taxi_id = t.id

SELECT p.*, t.driver_name , t.car_type FROM passengers p  
LEFT join taxis t ON p.taxi_id = t.id WHERE p.taxi_id is NULL

SELECT p.*, t.driver_name , t.car_type FROM passengers p  
FULL join taxis t ON p.taxi_id = t.id

SELECT p.*, t.driver_name , t.car_type FROM passengers p  
CROSS join taxis t 


