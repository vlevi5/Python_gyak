CREATE TABLE filmek (
 	filmid INT,
    cim VARCHAR(255) NOT NULL,
    ev INT NOT NULL,
    premier DATETIME NOT NULL,
    elozmeny INT,
    PRIMARY KEY (filmid)
);