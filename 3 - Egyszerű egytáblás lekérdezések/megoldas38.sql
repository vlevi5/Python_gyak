/* Saját megoldás ↓

SELECT YEAR(felveve)-YEAR(szuletett) AS felvetelkori_eletkor
FROM tanarok;

*/ 

SELECT DATEDIFF(felveve, szuletett) / 365
FROM tanarok;