SELECT fizetes, evek, kepesites
FROM fizetesek
WHERE kepesites IS NOT NULL
ORDER BY fizetes ASC LIMIT 3;