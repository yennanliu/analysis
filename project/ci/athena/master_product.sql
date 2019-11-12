CREATE EXTERNAL TABLE `master_product`(
  `product_code` string, 
  `product_type_code` string, 
  `product_classification_code` string, 
  `product_maker_code` string, 
  `genre_code` string, 
  `container_capacity_code` string, 
  `capacity` string, 
  `hot_cold_classification_product` string, 
  `release_date` string,
  `end_sales_date` string, 
  `standard_selling_price` string)
ROW FORMAT DELIMITED 
  FIELDS TERMINATED BY ',' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://<s3_bucket>/<s3_file>'
TBLPROPERTIES (
  'has_encrypted_data'='false', 
  'skip.header.line.count'='1', 
  'transient_lastDdlTime'='1573095479')