CREATE EXTERNAL TABLE `vm_portofolio`(
  `group_company_code` string, 
  `organization_group_code` string, 
  `customer_number` string, 
  `branch_number` string, 
  `equipment_code` string, 
  `product_code` string, 
  `column_no` string, 
  `sales_date` string)
ROW FORMAT DELIMITED 
  FIELDS TERMINATED BY ',' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://suntory-data/Aggregated_VM_month_portofolio'
TBLPROPERTIES (
  'has_encrypted_data'='false', 
  'skip.header.line.count'='1', 
  'transient_lastDdlTime'='1575422992')


