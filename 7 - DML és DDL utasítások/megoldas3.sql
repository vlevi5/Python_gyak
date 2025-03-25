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