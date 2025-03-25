SELECT fizetes*0.65 AS netto_fizetes, fizetes*0.65+15000 AS netto_fizetes_bonusszal
FROM fizetesek
WHERE kepesites LIKE "alapdiploma";