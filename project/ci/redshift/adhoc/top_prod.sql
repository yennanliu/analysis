WITH trans AS
  (SELECT *
   FROM public.filtered_9000_vm_transaction_201901
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201902
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201903
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201904
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201905
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201906)
SELECT product_code,
       sum(sales_quantity) as sum_sales_quantity,
       count(equipment_code) as count_vm
FROM trans
GROUP BY 1
ORDER BY 2 DESC;

