WITH trans AS
  (SELECT *
   FROM public.filtered_9000_vm_transaction_201401
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201402
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201403
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201404
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201405
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201406
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201407
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201408
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201409
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201410
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201411
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201412
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201501
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201502
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201503
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201504
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201505
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201506
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201507
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201508
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201509
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201510
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201511
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201512
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201601
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201602
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201603
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201604
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201605
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201606
   UNION ALL SELECT * 
   FROM public.filtered_9000_vm_transaction_201607
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201608
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201609
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201610
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201611
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201612
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201701
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201702
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201703
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201704
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201705
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201706
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201607
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201708
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201709
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201710
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201711
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201712
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201801
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201802
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201803
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201804
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201805
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201806
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201807
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201808
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201809
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201810
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201811
   UNION ALL SELECT *
   FROM public.filtered_9000_vm_transaction_201812
   UNION ALL SELECT *
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
SELECT equipment_code AS equipment_code_,
       product_code AS product_code_,
       column_no,
       sales_date AS laste_sales_date,
       *
FROM trans
WHERE (equipment_code,
       sales_date) IN
    (SELECT equipment_code,
            max(sales_date) AS sales_date
     FROM trans
     GROUP BY 1); 
