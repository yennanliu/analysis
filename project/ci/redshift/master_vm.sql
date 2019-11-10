-- drop
DROP TABLE if EXISTS master_vm;

-- create
CREATE TABLE master_vm(
  nnp_group_company_code VARCHAR(30), 
  nnp_organization_group_code VARCHAR(30), 
  equipment_code VARCHAR(30), 
  customer_number VARCHAR(30), 
  branch_number VARCHAR(30), 
  model_code VARCHAR(30), 
  model_year VARCHAR(30), 
  number_of_cell VARCHAR(30), 
  hot_selection_number VARCHAR(30), 
  number_of_buttons VARCHAR(30), 
  number_of_column_rows VARCHAR(30), 
  model_500_pet_selection VARCHAR(30), 
  model_500_cans_selection VARCHAR(30), 
  installation_date VARCHAR(30), 
  withdrawal_date VARCHAR(30),
  annual_contribution_sales_basis VARCHAR(30), 
  annual_contribution_sales_tax_excluded_amount VARCHAR(30), 
  customer_zip_code VARCHAR(30), 
  prefecture_code VARCHAR(30), 
  city_code VARCHAR(30), 
  buying_place_code VARCHAR(30), 
  in_out_classification VARCHAR(30), 
  open_closed_classification VARCHAR(30), 
  basic_organization_code VARCHAR(30), 
  delivery_route_code VARCHAR(30), 
  group_company_code VARCHAR(30), 
  column_no VARCHAR(30), 
  column_position_row VARCHAR(30), 
  column_position_column VARCHAR(30), 
  hot_switchable_flag VARCHAR(30), 
  capacity_100_160_cans VARCHAR(30), 
  capacity_110_190_cans VARCHAR(30), 
  capacity_120_230_cans VARCHAR(30), 
  capacity_130_280_cans VARCHAR(30), 
  capacity_140_american_size_can VARCHAR(30), 
  capacity_130_bottle_can_small VARCHAR(30), 
  capacity_160_small_capacity_pet_small VARCHAR(30), 
  capacity_170_120_81e_180_bottles VARCHAR(30), 
  capacity_180_210_81e_220_bottles VARCHAR(30), 
  capacity_190_bottle_can_large VARCHAR(30),
  capacity_200_small_capacity_pet_large VARCHAR(30), 
  capacity_210_long_can VARCHAR(30), 
  capacity_220_300ml_pet VARCHAR(30), 
  capacity_225_435ml_pet VARCHAR(30)
  );

-- copy
copy master_vm
from 's3://suntory-data/raw_master_vm/' 
iam_role 'arn:aws:iam::xxxxxxx'
IGNOREHEADER 1 delimiter ',';
