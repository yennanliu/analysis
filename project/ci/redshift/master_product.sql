-- drop
DROP TABLE if EXISTS master_product;

-- create 
CREATE TABLE master_product(
  product_code VARCHAR(10), 
  product_type_code VARCHAR(10),  
  product_classification_code VARCHAR(10), 
  product_maker_code VARCHAR(10), 
  genre_code VARCHAR(10), 
  container_capacity_code VARCHAR(10), 
  capacity VARCHAR(10), 
  hot_cold_classification_product VARCHAR(10), 
  release_date VARCHAR(10), 
  end_sales_date VARCHAR(10),  
  standard_selling_price VARCHAR(10));

-- copy 
copy master_product
from 's3://suntory-data/raw_master_product/' 
iam_role 'arn:aws:iam::xxxxxxx'
IGNOREHEADER 1 delimiter ',';