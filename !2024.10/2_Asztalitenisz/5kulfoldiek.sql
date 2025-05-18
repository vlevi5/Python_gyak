SELECT egyesulet.orszag
FROM egyesulet, bajnok, jatekos
WHERE egyesulet.id = bajnok.egyesulet_id
    AND bajnok.ev > 2000
    AND egyesulet.orszag NOT LIKE "Magyarország"
    GROUP BY egyesulet.orszag;