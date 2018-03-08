
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




-- day total searching  with specific periods and ldn area 


SELECT cast(substring(search_time_utc,
         1,
         10) AS date) as date,
         count(*) as search_count
FROM vehicle_search_responses
WHERE search_time_utc IS NOT NULL
        AND cast(substring(search_time_utc, 1, 10) AS date) > cast('2017-01-01' AS date)
        AND cast(search_lat AS integer) > 50
        AND cast(search_lat AS integer) < 52
GROUP BY  1
ORDER BY  1 LIMIT 3000






