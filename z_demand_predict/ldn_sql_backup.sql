
-- Athena SQL 

/*

doc : 

-- https://docs.aws.amazon.com/redshift/latest/dg/cm_chap_SQLCommandRef.html


*/



-- day total searching 

SELECT substring(start_time_utc,
        1,
        10),
         count(*)
FROM vehicle_search_responses
WHERE start_time_utc is NOT null
GROUP BY  1
ORDER BY  1 limit 1000 



-- dev 













