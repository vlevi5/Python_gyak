SELECT jatekos.nev, MAX(bajnok.ev)-MIN(bajnok.ev) eltelt_ev
FROM bajnok, jatekos
WHERE jatekos.id = bajnok.jatekos_id
GROUP BY jatekos.id
HAVING  eltelt_ev >= 10
ORDER BY eltelt_ev DESC;