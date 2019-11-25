WITH aggre_t AS
  (SELECT SUBSTRING(sales_date, 1, 7) AS sales_month,
          branch_number,
          customer_number,
          equipment_code,
          column_no,
          sum(sales_quantity) AS sales_quantity,
          sum(sales_after_supply) AS sales_after_supply
   FROM target_vm_9000_vm_transaction_201901
   GROUP BY 1,
            2,
            3,
            4,
            5),
     t AS
  (SELECT SUBSTRING(sales_date, 1, 7) AS sales_month,
          *
   FROM target_vm_9000_vm_transaction_201901)
SELECT aggre_t.sales_quantity,
       aggre_t.sales_after_supply,
       t.*
FROM aggre_t
INNER JOIN t ON t.sales_month = aggre_t.sales_month
AND t.branch_number = aggre_t.branch_number
AND t.customer_number = aggre_t.customer_number
AND t.column_no = aggre_t.column_no
LIMIT 100;

