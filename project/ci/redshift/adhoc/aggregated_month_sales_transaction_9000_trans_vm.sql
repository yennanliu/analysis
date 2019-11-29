-----------------------------------
-- V1 
-----------------------------------

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

-----------------------------------
-- V2
-----------------------------------

-- WITH aggre_t AS
--   (SELECT SUBSTRING(sales_date, 1, 7) AS sales_month,
--           branch_number,
--           customer_number,
--           equipment_code,
--           column_no,
--           product_code,
--           site_code ,
--           department_code ,
--           route_code ,
--           customer_number ,
--           group_company_code ,
--           selling_price ,
--           meter_no ,
--           hot_cold_classification ,
--           buying_place_code ,
--           sales_system_representative_code ,
--           sales_method_detail_code ,
--           in_out_classification ,
--           annual_contribution_sales_capacity_conversion,
--           open_closed_classification ,
--           contents_manufacturer_code ,
--           installation_date ,
--           number_of_adjacent_vm_cc,
--           number_of_adjacent_vm_k,
--           number_of_adjacent_vm_a,
--           number_of_adjacent_vm_dy,
--           number_of_adjacent_vm_it,
--           number_of_adjacent_vm_po,
--           number_of_adjacent_vm_ot,
--           number_of_adjacent_vm_sf,
--           sum(sales_quantity) AS sales_quantity
--    FROM target_vm_9000_vm_transaction_201901
--    GROUP BY 1,
--             2,
--             3,
--             4,
--             5,
--             6,
--             7,
--             8,
--             9,
--             10,
--             11,
--             12,
--             13,
--             14,
--             15,
--             16,
--             17,
--             18,
--             19,
--             20,
--             21,
--             22,
--             23,
--             24,
--             25,
--             26,
--             27,
--             28,
--             29,
--             30)
-- SELECT *
-- FROM aggre_t limit 1000; 

-----------------------------------
-- V3
-----------------------------------

-- WITH filtered_vm AS
--   (SELECT sales_date,
--           branch_number,
--           customer_number,
--           equipment_code,
--           count(DISTINCT product_code)::numeric/max(column_no)::numeric AS item_ratio
--    FROM target_vm_9000_vm_transaction_201812
--    GROUP BY 1,
--             2,
--             3,
--             4
--    HAVING item_ratio > 0.5),
--      filtered_t AS
--   (SELECT *
--    FROM target_vm_9000_vm_transaction_201812
--    WHERE (sales_date,
--           branch_number,
--           customer_number,
--           equipment_code) IN
--        (SELECT sales_date,
--                branch_number,
--                customer_number,
--                equipment_code
--         FROM filtered_vm) ),
--      aggre_t AS
--   (SELECT SUBSTRING(sales_date, 1, 7) AS sales_month,
--           branch_number,
--           customer_number,
--           equipment_code,
--           column_no,
--           product_code,
--           site_code,
--           department_code,
--           route_code,
--           customer_number,
--           group_company_code,
--           selling_price,
--           meter_no,
--           hot_cold_classification,
--           buying_place_code,
--           sales_system_representative_code,
--           sales_method_detail_code,
--           in_out_classification,
--           annual_contribution_sales_capacity_conversion,
--           open_closed_classification,
--           contents_manufacturer_code,
--           installation_date,
--           product_code_before_replacement,
--           hot_cold_classification_before_product_replacement AS hot_cold_classification_before_replacement,
--           number_of_sales_update_failure,
--           number_of_adjacent_vm_cc,
--           number_of_adjacent_vm_k,
--           number_of_adjacent_vm_a,
--           number_of_adjacent_vm_dy,
--           number_of_adjacent_vm_it,
--           number_of_adjacent_vm_po,
--           number_of_adjacent_vm_ot,
--           number_of_adjacent_vm_sf,
--           sum(sales_quantity) AS sales_quantity
--    FROM filtered_t
--    WHERE number_of_sales_update_failure = 0
--      AND sales_quantity < 1000
--    GROUP BY 1,
--             2,
--             3,
--             4,
--             5,
--             6,
--             7,
--             8,
--             9,
--             10,
--             11,
--             12,
--             13,
--             14,
--             15,
--             16,
--             17,
--             18,
--             19,
--             20,
--             21,
--             22,
--             23,
--             24,
--             25,
--             26,
--             27,
--             28,
--             29,
--             30,
--             31,
--             32,
--             33)
-- SELECT *
-- FROM aggre_t;

-----------------------------------
-- V4
-----------------------------------

WITH master_vm AS
  (SELECT *
   FROM public.master_vm),
     filtered_vm AS
  (SELECT SUBSTRING(tr.sales_date, 1, 7) AS sales_month,
          tr.branch_number,
          tr.customer_number,
          tr.equipment_code,
          tr.group_company_code,
          master_vm.nnp_organization_group_code as organization_group_code,
          count(DISTINCT tr.product_code)::numeric/max(tr.column_no)::numeric AS item_ratio
   FROM transaction_201901 tr
   INNER JOIN master_vm ON master_vm.group_company_code = tr.group_company_code
   AND master_vm.customer_number = tr.customer_number
   AND master_vm.branch_number = tr.branch_number
   AND master_vm.equipment_code = tr.equipment_code
   WHERE tr.number_of_sales_update_failure = 0
     AND tr.sales_quantity < 1000
    GROUP BY 1,2,3,4,5,6 
     HAVING item_ratio > 0.5),
     filtered_t AS
  (SELECT *
   FROM transaction_201901
   WHERE (
          branch_number,
          customer_number,
          group_company_code,
          equipment_code) IN
       (SELECT 
               branch_number,
               customer_number,
               group_company_code,
               equipment_code
        FROM filtered_vm) ),
     aggre_t AS
  (SELECT SUBSTRING(sales_date, 1, 7) AS sales_month,
          branch_number,
          customer_number,
          equipment_code,
          organization_group_code,
          column_no,
          product_code,
          site_code,
          department_code,
          route_code,
          customer_number,
          group_company_code,
          selling_price,
          meter_no,
          hot_cold_classification,
          buying_place_code,
          sales_system_representative_code,
          sales_method_detail_code,
          in_out_classification,
          annual_contribution_sales_capacity_conversion,
          open_closed_classification,
          contents_manufacturer_code,
          installation_date,
          product_code_before_replacement,
          hot_cold_classification_before_product_replacement AS hot_cold_classification_before_replacement,
          number_of_sales_update_failure,
          number_of_adjacent_vm_cc,
          number_of_adjacent_vm_k,
          number_of_adjacent_vm_a,
          number_of_adjacent_vm_dy,
          number_of_adjacent_vm_it,
          number_of_adjacent_vm_po,
          number_of_adjacent_vm_ot,
          number_of_adjacent_vm_sf,
          sum(sales_quantity) AS sales_quantity
   FROM filtered_t
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
            30,
            31,
            32,
            33,
            34)
SELECT *
FROM aggre_t;
