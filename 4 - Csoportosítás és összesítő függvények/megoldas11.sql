SELECT evfolyam, osztaly, COUNT(*) AS diakok_szama
FROM diakok
GROUP BY evfolyam, osztaly;