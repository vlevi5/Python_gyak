SELECT( 
    SELECT COUNT(diakok.id)
	FROM diakok
	WHERE diakok.nem = 'F'
    GROUP BY diakok.nem) -
    (SELECT COUNT(diakok.id)
	FROM diakok
	WHERE diakok.nem = 'N'
    GROUP BY diakok.nem) AS kulonbseg;