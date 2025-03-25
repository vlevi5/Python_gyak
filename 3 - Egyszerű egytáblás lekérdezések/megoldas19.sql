SELECT fizetes, evek, kepesites
FROM fizetesek
WHERE (kepesites = "alapdiploma" OR kepesites = "mesterdiploma") AND evek > 10;