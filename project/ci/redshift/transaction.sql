-- drop 
DROP TABLE if EXISTS transaction ;

-- create
CREATE TABLE transaction( 
    group_company_code  VARCHAR (10),
    wireless_sales_slip_no INTEGER,
    column_no        INTEGER,
    product_code     INTEGER,
    full_tank_number INTEGER,
    selling_price    INTEGER,
    meter_no         INTEGER,
    hot_cold_classification  VARCHAR (5),
    last_visit_inventory VARCHAR (5),
    sales_quantity   VARCHAR (5),
    sales_after_supply VARCHAR (5),
    product_code_before_replacement VARCHAR (10),
    full_tank_quantity_before_product_replacement VARCHAR (10),
    number_of_products_introduced_before_product_replacement VARCHAR (10),
    price_before_replacement  VARCHAR (10),
    meter_no_before_product_replacement  VARCHAR (10),
    hot_cold_classification_before_product_replacement VARCHAR (10),
    site_code        INTEGER,
    department_code  INTEGER,
    route_code       INTEGER, 
    customer_number  INTEGER,
    branch_number    INTEGER,
    equipment_code   INTEGER,
    sales_date TIMESTAMP, 
    last_visit_date TIMESTAMP, 
    last_calibration_date VARCHAR (20), 
    number_of_sales_update_failure  INTEGER, 
    buying_place_code  VARCHAR (5),
    sales_system_representative_code  INTEGER,
    sales_method_detail_code  INTEGER,
    in_out_classification     NUMERIC,
    annual_contribution_sales_capacity_conversion INTEGER, 
    open_closed_classification VARCHAR (30),
    contents_manufacturer_code VARCHAR (30),
    installation_date         TIMESTAMP,
    number_of_adjacent_vm_cc  NUMERIC, 
    number_of_adjacent_vm_k   NUMERIC, 
    number_of_adjacent_vm_a   NUMERIC, 
    number_of_adjacent_vm_dy  NUMERIC, 
    number_of_adjacent_vm_it  NUMERIC, 
    number_of_adjacent_vm_po  NUMERIC, 
    number_of_adjacent_vm_ot  NUMERIC, 
    number_of_adjacent_vm_sf  NUMERIC 
    );

-- copy
copy transaction
from 's3://suntory-data/raw_transaciton_data/' 
iam_role 'arn:aws:iam::xxxxxxx'
IGNOREHEADER 1 delimiter ',';