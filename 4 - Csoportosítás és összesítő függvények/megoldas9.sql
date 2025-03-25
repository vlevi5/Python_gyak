SELECT targy, COUNT(*) AS db	
FROM oktatott
GROUP BY targy
ORDER BY db DESC LIMIT 1;