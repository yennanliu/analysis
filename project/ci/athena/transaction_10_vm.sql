CREATE EXTERNAL TABLE `transaction_10_vm`(
  `group_company_code` string COMMENT 'from deserializer', 
  `wireless_sales_slip_no` string COMMENT 'from deserializer', 
  `column_no` string COMMENT 'from deserializer', 
  `product_code` string COMMENT 'from deserializer', 
  `full_tank_number` string COMMENT 'from deserializer', 
  `selling_price` string COMMENT 'from deserializer', 
  `meter_no` string COMMENT 'from deserializer', 
  `hot_cold_classification` string COMMENT 'from deserializer', 
  `last_visit_inventory` string COMMENT 'from deserializer', 
  `sales_quantity` string COMMENT 'from deserializer', 
  `sales_after_supply` string COMMENT 'from deserializer', 
  `product_code_before_replacement` string COMMENT 'from deserializer', 
  `full_tank_quantity_before_product_replacement` string COMMENT 'from deserializer', 
  `number_of_products_introduced_before_product_replacement` string COMMENT 'from deserializer', 
  `price_before_replacement` string COMMENT 'from deserializer', 
  `meter_no_before_product_replacement` string COMMENT 'from deserializer', 
  `hot_cold_classification_before_product_replacement` string COMMENT 'from deserializer', 
  `site_code` string COMMENT 'from deserializer', 
  `department_code` string COMMENT 'from deserializer', 
  `route_code` string COMMENT 'from deserializer', 
  `customer_number` string COMMENT 'from deserializer', 
  `branch_number` string COMMENT 'from deserializer', 
  `equipment_code` string COMMENT 'from deserializer', 
  `sales_date` string COMMENT 'from deserializer', 
  `last_visit_date` string COMMENT 'from deserializer', 
  `last_calibration_date` string COMMENT 'from deserializer', 
  `number_of_sales_update_failure` string COMMENT 'from deserializer', 
  `buying_place_code` string COMMENT 'from deserializer', 
  `sales_system_representative_code` string COMMENT 'from deserializer', 
  `sales_method_detail_code` string COMMENT 'from deserializer', 
  `in_out_classification` string COMMENT 'from deserializer', 
  `annual_contribution_sales_capacity_conversion` string COMMENT 'from deserializer', 
  `open_closed_classification` string COMMENT 'from deserializer', 
  `contents_manufacturer_code` string COMMENT 'from deserializer', 
  `installation_date` string COMMENT 'from deserializer', 
  `number_of_adjacent_vm_cc` string COMMENT 'from deserializer', 
  `number_of_adjacent_vm_k` string COMMENT 'from deserializer', 
  `number_of_adjacent_vm_a` string COMMENT 'from deserializer', 
  `number_of_adjacent_vm_dy` string COMMENT 'from deserializer', 
  `number_of_adjacent_vm_it` string COMMENT 'from deserializer', 
  `number_of_adjacent_vm_po` string COMMENT 'from deserializer', 
  `number_of_adjacent_vm_ot` string COMMENT 'from deserializer', 
  `number_of_adjacent_vm_sf` string COMMENT 'from deserializer', 
  `other_num` string COMMENT 'from deserializer', 
  `dt` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.serde2.OpenCSVSerde' 
WITH SERDEPROPERTIES ( 
  'escapeChar'='\\', 
  'quoteChar'='\"', 
  'separatorChar'=',') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://suntory-data/filtered_10_vm_transaction'
TBLPROPERTIES (
  'has_encrypted_data'='false', 
  'skip.header.line.count'='1', 
  'transient_lastDdlTime'='1573463860')