WITH t AS
  (SELECT SUBSTRING(sales_date, 1, 7) AS sales_month,
          group_company_code,
          wireless_sales_slip_no,
          column_no ,
          product_code ,
          full_tank_number,
          selling_price ,
          meter_no ,
          hot_cold_classification,
          last_visit_inventory,
          sales_quantity ,
          sales_after_supply,
          hot_cold_classification_before_product_replacement,
          site_code ,
          department_code,
          route_code ,
          customer_number,
          branch_number ,
          equipment_code ,
          last_visit_date,
          last_calibration_date,
          buying_place_code,
          in_out_classification,
          annual_contribution_sales_capacity_conversion,
          open_closed_classification,
          contents_manufacturer_code,
          installation_date ,
          sum(sales_quantity) AS sales_quantity,
          sum(sales_after_supply) AS sales_after_supply
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
            27),
     p AS
  (SELECT *
   FROM master_product),
     v AS
  (SELECT *
   FROM master_vm)
SELECT t.*,
       p.*,
       v.*
FROM t
INNER JOIN p ON t.product_code = p.product_code
INNER JOIN v ON v.equipment_code = t.equipment_code
AND v.column_no = t.column_no
LIMIT 100;