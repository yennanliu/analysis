CREATE OR REPLACE VIEW filtered_10_vm_transaction_2019 AS 
WITH
  t_2019 AS (
   SELECT *
   FROM
     suntory.transaction
   WHERE ((("dt" >= '201901') AND ("dt" <= '201912')) AND ("equipment_code" IN ('42090952', '41092022', '1935412', '42009195', '410091', '42109499', '42099432', '1934993', '1911952', '42011429')))
) 
SELECT *
FROM
  t_2019
