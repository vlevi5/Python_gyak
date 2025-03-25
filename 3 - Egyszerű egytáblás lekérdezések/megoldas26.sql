SELECT *
FROM oktatott
WHERE heti NOT BETWEEN "3" AND "5" OR targy = "matek"
ORDER BY heti ASC, targy ASC;