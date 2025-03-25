SELECT fizetes, fizetes * 0.65 + 15000 + fizetes*0.35*(0.01*evek) AS netto_fizetes_bonusszal_adovisszateritessel, fizetes*0.35*(0.01*evek) AS bonusz_erteke
FROM fizetesek
WHERE kepesites = 'mesterdiploma';