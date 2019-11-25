create external table spectrum.target_vm(
organization_group_code VARCHAR(10),
management_name VARCHAR(10),
site_code VARCHAR(10),
route_code VARCHAR(10),
customer_number VARCHAR(10),
branch_number VARCHAR(10),
equipment_code VARCHAR(10),
sf_no VARCHAR(10),
model_code VARCHAR(10),
installation_date VARCHAR(10),
free_bend_classification VARCHAR(10),
wireless_open_flag VARCHAR(10),
customer_zip_code VARCHAR(10),
prefecture_code VARCHAR(10),
city_code VARCHAR(10),
customer_phone_number VARCHAR(10),
buying_place_code VARCHAR(10),
transaction_start_date VARCHAR(10),
in_out_classification VARCHAR(10),
open_closed_classification VARCHAR(10),
annual_contribution_sales_basis VARCHAR(10),
in_house VARCHAR(10),
model_year VARCHAR(10),
number_of_cell VARCHAR(10),
hot_selection_number VARCHAR(10),
number_of_buttons VARCHAR(10),
number_of_column_rows VARCHAR(10),
model_500_pet_selection VARCHAR(10),
model_500_cans_selection VARCHAR(10),
group_company_code VARCHAR(10),
column_no VARCHAR(10),
column_position_row VARCHAR(10),
column_position_column VARCHAR(10)
)
row format delimited
fields terminated by ',' 
stored as textfile
location 's3://suntory-data/target_vm/'
table properties ('skip.header.line.count'='1');
