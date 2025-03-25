SELECT DATEDIFF(NOW(), beirva) AS eltelt_napok
FROM jegyek
ORDER BY beirva DESC
LIMIT 1;