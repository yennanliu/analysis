DROP TABLE if EXISTS master_product;

CREATE TABLE master_product(
  product_code VARCHAR (10), 
  product_type_code VARCHAR (10),  
  product_classification_code VARCHAR (10), 
  product_maker_code VARCHAR (10), 
  genre_code VARCHAR (10), 
  kanji_official_name  VARCHAR (10), 
  container_capacity_code VARCHAR (10), 
  capacity VARCHAR (10), 
  hot_cold_classification_product VARCHAR (10), 
  release_date VARCHAR (10), 
  end_sales_date VARCHAR (10),  
  standard_selling_price VARCHAR (10));