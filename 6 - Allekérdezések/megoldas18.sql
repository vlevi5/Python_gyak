SELECT ROUND(AVG(darab),2) AS atlag
FROM (SELECT COUNT(diakok.id) AS darab
	  FROM diakok
	  GROUP BY diakok.evfolyam
) AS diakok_evfolyamonkent;