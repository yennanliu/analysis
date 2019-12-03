create external table spectrum.vm_capacity(
model_code VARCHAR(10),
column_no INTEGER,
column_position_row INTEGER,
column_position_column INTEGER,
hot_switchable_flag INTEGER,
capacity_100 INTEGER,
capacity_110 INTEGER,
capacity_120 INTEGER,
capacity_130 INTEGER,
capacity_140 INTEGER,
capacity_150 INTEGER,
capacity_160 INTEGER,
capacity_170 INTEGER,
capacity_180 INTEGER,
capacity_190 INTEGER,
capacity_200 INTEGER,
capacity_210 INTEGER,
capacity_220 INTEGER,
capacity_225 INTEGER
)
row format delimited
fields terminated by ',' 
stored as textfile
location 's3://suntory-data/Rawdata_vm_capacity/'
table properties ('skip.header.line.count'='1');
