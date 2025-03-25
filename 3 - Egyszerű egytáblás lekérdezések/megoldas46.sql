SELECT nev, szuletett, YEAR(szuletett) + 7 + 12 + 2 AS diploma_varhato_eve
FROM tanarok
ORDER BY szuletett ASC;