create external table spectrum.vm_list(
index VARCHAR(10),
vm_id VARCHAR(10))
row format delimited
fields terminated by ',' 
stored as textfile
location 's3://suntory-data/vm_list_5271/'
table properties ('skip.header.line.count'='1');