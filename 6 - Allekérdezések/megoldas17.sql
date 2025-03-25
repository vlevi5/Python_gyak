SELECT EXISTS (
    SELECT diakok.id
    FROM diakok LEFT JOIN jegyek ON diakok.id = jegyek.diakid
    WHERE osztalyzat IS NULL
) AS letezik;

