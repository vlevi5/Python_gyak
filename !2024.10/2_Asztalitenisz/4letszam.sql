SELECT IF(jatekos.neme=0, "nő", "férfi") as nem, COUNT(*) AS fő
FROM jatekos
GROUP BY jatekos.neme;