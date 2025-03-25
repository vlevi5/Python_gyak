SELECT fizetes, fizetes * 0.65 + 15000 + fizetes*0.35*(0.01*evek) AS netto, fizetes*0.35*(0.01*evek) AS jutalek
FROM fizetesek
WHERE kepesites = 'mesterdiploma'
ORDER BY netto DESC;