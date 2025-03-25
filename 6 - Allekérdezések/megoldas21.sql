SELECT
    ROUND(
        DATEDIFF(NOW(), tanarok.szuletett) -
        (SELECT AVG(DATEDIFF(NOW(), szuletett)) FROM tanarok)
    ) AS elteres
FROM tanarok;