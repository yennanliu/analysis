SELECT 
t.*,
v.*,
p.*
FROM "suntory"."transaction_10_vm" as t 
left join 
"suntory"."master_vm" as v
on v.equipment_code  =  t.equipment_code
and v.column_no  =  t.column_no
left join 
"suntory"."master_product" as p
on t.product_code  =  p.product_code
;