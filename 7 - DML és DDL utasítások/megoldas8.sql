UPDATE vetitesek
SET terem = "1"
WHERE filmid = 6;

/* -- VAGY --

UPDATE vetitesek, filmek
SET terem = 1
WHERE vetitesek.filmid = filmek.filmid
AND cim = 'Terminator 2: Judgment Day';

*/

