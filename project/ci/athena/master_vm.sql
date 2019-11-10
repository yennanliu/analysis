CREATE EXTERNAL TABLE `master_vm`(
  `nnp_group_company_code` string, 
  `nnp_organization_group_code` string, 
  `equipment_code` string, 
  `customer_number` string, 
  `branch_number` string, 
  `model_code` string, 
  `model_year` string, 
  `number_of_cell` string, 
  `hot_selection_number` string, 
  `number_of_buttons` string, 
  `number_of_column_rows` string, 
  `model_500_pet_selection` string, 
  `model_500_cans_selection` string, 
  `installation_date` string, 
  `withdrawal_date` string, 
  `annual_contribution_sales_basis` string, 
  `annual_contribution_sales_tax_excluded_amount` string, 
  `customer_zip_code` string, 
  `prefecture_code` string, 
  `city_code` string, 
  `buying_place_code` string, 
  `in_out_classification` string, 
  `open_closed_classification` string, 
  `basic_organization_code` string, 
  `delivery_route_code` string, 
  `group_company_code` string, 
  `column_no` string, 
  `column_position_row` string, 
  `column_position_column` string, 
  `hot_switchable_flag` string, 
  `capacity_100_160_cans` string, 
  `capacity_110_190_cans` string, 
  `capacity_120_250_cans` string, 
  `capacity_130_280_cans` string, 
  `capacity_140_american_size_can` string, 
  `capacity_150_bottle_can_small` string, 
  `capacity_160_small_capacity_pet_small` string, 
  `capacity_170_120_81e_180_bottles` string, 
  `capacity_180_210_81e_220_bottles` string, 
  `capacity_190_bottle_can_large` string, 
  `capacity_200_small_capacity_pet_large` string, 
  `capacity_210_long_can` string, 
  `capacity_220_500ml_pet` string, 
  `capacity_225_435ml_pet` string)
ROW FORMAT DELIMITED 
  FIELDS TERMINATED BY ',' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://suntory-data/raw_master_vm'
TBLPROPERTIES (
  'has_encrypted_data'='false', 
  'transient_lastDdlTime'='1573351370')