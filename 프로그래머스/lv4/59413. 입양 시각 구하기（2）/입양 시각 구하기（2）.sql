SELECT HOUR, SUM(COUNT) "COUNT"
    FROM (
            SELECT HOUR(DATETIME) HOUR, COUNT(*) "COUNT"
                FROM ANIMAL_OUTS
                GROUP BY HOUR(DATETIME)

            UNION SELECT 0 HOUR, 0
            UNION SELECT 1 HOUR, 0
            UNION SELECT 2 HOUR, 0
            UNION SELECT 3 HOUR, 0
            UNION SELECT 4 HOUR, 0
            UNION SELECT 5 HOUR, 0
            UNION SELECT 6 HOUR, 0
            UNION SELECT 7 HOUR, 0
            UNION SELECT 8 HOUR, 0
            UNION SELECT 9 HOUR, 0
            UNION SELECT 10 HOUR, 0
            UNION SELECT 11 HOUR, 0
            UNION SELECT 12 HOUR, 0
            UNION SELECT 13 HOUR, 0
            UNION SELECT 14 HOUR, 0
            UNION SELECT 15 HOUR, 0
            UNION SELECT 16 HOUR, 0
            UNION SELECT 17 HOUR, 0
            UNION SELECT 18 HOUR, 0
            UNION SELECT 19 HOUR, 0
            UNION SELECT 20 HOUR, 0
            UNION SELECT 21 HOUR, 0
            UNION SELECT 22 HOUR, 0
            UNION SELECT 23 HOUR, 0
        ) A
    GROUP BY HOUR
    ORDER BY HOUR
