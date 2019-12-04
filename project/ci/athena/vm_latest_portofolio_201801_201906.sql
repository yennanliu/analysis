with latest AS 
    (SELECT group_company_code,
         organization_group_code,
         customer_number,
         branch_number,
         equipment_code,
         max(sales_date) AS sales_date
    FROM "suntory"."vm_portofolio_201801_201906"
    GROUP BY  1,2,3,4,5 )
SELECT tr.group_company_code,
         tr.organization_group_code,
         tr.customer_number,
         tr.branch_number,
         tr.equipment_code,
         tr.product_code,
         tr.sales_date
FROM "suntory"."vm_portofolio_201801_201906" tr
INNER JOIN latest
    ON latest.group_company_code = tr.group_company_code
        AND latest.organization_group_code = tr.organization_group_code
        AND latest.customer_number = tr.customer_number
        AND latest.branch_number = tr.branch_number
        AND latest.equipment_code = tr.equipment_code
        AND latest.sales_date = tr.sales_date