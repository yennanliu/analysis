-- drop
DROP TABLE if EXISTS master_vm;

-- create
CREATE TABLE master_vm(
  nnp_group_company_code VARCHAR(30),
  nnp_organization_group_code VARCHAR(30),
  equipment_code VARCHAR(30),
  customer_number VARCHAR(30),
  Branch_number VARCHAR(30),
  num_of_selection VARCHAR(30),
  num_of_hot_selection VARCHAR(30),
  num_of_buttons VARCHAR(30),
  num_of_position_rows VARCHAR(30),
  num_of_500_pet_selection VARCHAR(30),
  num_of_500_cans_selection VARCHAR(30),
  start_date_vm VARCHAR(30),
  end_date_vm VARCHAR(30),
  frag_free_vend VARCHAR(30),
  fundraising_vm_category VARCHAR(30),
  annual_sales_quantity_box VARCHAR(30),
  annual_sales_quantity VARCHAR(30),
  annual_sales_amount_tax_excluded VARCHAR(30),
  prefecture_code VARCHAR(30),
  city_code VARCHAR(30),
  buying_place_code VARCHAR(30),
  in_out_classification VARCHAR(30),
  open_closed_classification VARCHAR(30),
  group_company_code VARCHAR(30)
  );

-- copy
copy master_vm
from 's3://suntory-data/Rawdata_master_vm/' 
iam_role 'arn:aws:iam::xxxxxxx'
IGNOREHEADER 1 delimiter ',';
