-- WITH aggre_t AS
--   (SELECT SUBSTRING(sales_date, 1, 7) AS sales_month,
--           branch_number,
--           customer_number,
--           equipment_code,
--           column_no,
--           sum(sales_quantity) AS sales_quantity,
--           sum(sales_after_supply) AS sales_after_supply
--    FROM target_vm_9000_vm_transaction_201901
--    GROUP BY 1,
--             2,
--             3,
--             4,
--             5),
--      t AS
--   (SELECT SUBSTRING(sales_date, 1, 7) AS sales_month,
--           *
--    FROM target_vm_9000_vm_transaction_201901)
-- SELECT aggre_t.sales_quantity,
--        aggre_t.sales_after_supply,
--        t.*
-- FROM aggre_t
-- INNER JOIN t ON t.sales_month = aggre_t.sales_month
-- AND t.branch_number = aggre_t.branch_number
-- AND t.customer_number = aggre_t.customer_number
-- AND t.column_no = aggre_t.column_no
-- LIMIT 100;

WITH aggre_t AS
  (SELECT SUBSTRING(sales_date, 1, 7) AS sales_month,
          branch_number,
          customer_number,
          equipment_code,
          column_no,
          product_code,
          site_code ,
          department_code ,
          route_code ,
          customer_number ,
          group_company_code ,
          selling_price ,
          meter_no ,
          hot_cold_classification ,
          buying_place_code ,
          sales_system_representative_code ,
          sales_method_detail_code ,
          in_out_classification ,
          annual_contribution_sales_capacity_conversion,
          open_closed_classification ,
          contents_manufacturer_code ,
          installation_date ,
          number_of_adjacent_vm_cc,
          number_of_adjacent_vm_k,
          number_of_adjacent_vm_a,
          number_of_adjacent_vm_dy,
          number_of_adjacent_vm_it,
          number_of_adjacent_vm_po,
          number_of_adjacent_vm_ot,
          number_of_adjacent_vm_sf,
          sum(sales_quantity) AS sales_quantity
   FROM target_vm_9000_vm_transaction_201901
   GROUP BY 1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
            22,
            23,
            24,
            25,
            26,
            27,
            28,
            29,
            30)
SELECT *
FROM aggre_t limit 1000; 
