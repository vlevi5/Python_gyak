DROP TABLE vetitesekek;

DROP TABLE filmek;

CREATE TABLE filmek (
 	filmid INT AUTO_INCREMENT,
    cim VARCHAR(255) NOT NULL,
    ev INT NOT NULL,
    premier DATETIME NOT NULL,
    elozmeny INT,
    PRIMARY KEY (filmid)
);

CREATE TABLE vetitesek (
	id INT AUTO_INCREMENT,
    filmid INT,
    kezdet DATETIME NOT NULL,
    veg DATETIME NOT NULL,
    terem INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (filmid)
    	REFERENCES filmek (filmid)
);