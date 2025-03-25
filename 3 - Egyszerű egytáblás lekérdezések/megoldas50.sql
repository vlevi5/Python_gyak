SELECT SUBSTRING(nev, 1, POSITION(" " IN nev)-1) AS vezeteknev, SUBSTRING(nev, POSITION(" " IN nev)+1) AS keresztnev, targyak, FLOOR(DATEDIFF(NOW(), szuletett)/365) AS eletkor
FROM tanarok;