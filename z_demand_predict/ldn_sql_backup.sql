
-- Athena SQL 

/*

doc : 

-- https://docs.aws.amazon.com/redshift/latest/dg/cm_chap_SQLCommandRef.html


*/



-- day total searching 

SELECT cast(substring(search_time_utc,
         1,
         10) AS date),
         count(*)
FROM vehicle_search_responses
WHERE search_time_utc is NOT null
GROUP BY  1
ORDER BY  1 limit 1000 



-- day total searching  with specific periods  

SELECT cast(substring(search_time_utc,
         1,
         10) AS date),
         count(*)
FROM vehicle_search_responses
WHERE search_time_utc is NOT null
        AND cast(substring(search_time_utc, 1, 10) AS date) > cast('2018-03-01' AS date)
GROUP BY  1
ORDER BY  1  limit 100
















