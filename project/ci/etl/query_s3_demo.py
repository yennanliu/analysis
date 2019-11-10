import sys
sys.path.append("./utility/")
import os
import pyspark
import math 
import pygeohash as pgh
from datetime import datetime
from pyspark.sql import SQLContext, Row
from pyspark import SparkContext
from pyspark.sql import functions as F
# UDF 
from utility import * 

os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages com.amazonaws:aws-java-sdk-pom:1.7.4,org.apache.hadoop:hadoop-aws:2.7.6 pyspark-shell'
# aws access
aws_creds = parse_config('config/s3.config')
AWSAccessKey = aws_creds['AWSAccessKey']
AWSSecretKey = aws_creds['AWSSecretKey']
sc = SparkContext.getOrCreate()
sc._jsc.hadoopConfiguration().set('fs.s3a.access.key', AWSAccessKey)
sc._jsc.hadoopConfiguration().set('fs.s3a.secret.key', AWSSecretKey)
sqlContext = pyspark.sql.SQLContext(sc)
# file url
s3_file_name =aws_creds['s3_file_name']

def main():
    data = sc.textFile(s3_file_name).map(lambda line: line.split(","))
    headers = data.first()
    data_ = data.filter(lambda row: row != headers and row != [''])  # fix null data 
    dataFrame = sqlContext.createDataFrame(data_,
            ['group_company_code', 'wireless_sales_slip_no', 'column_no',
           'product_code', 'full_tank_number', 'selling_price', 'meter_no',
           'hot_cold_classification', 'last_visit_inventory', 'sales_quantity',
           'sales_after_supply', 'product_code_before_replacement',
           'full_tank_quantity_before_product_replacement',
           'number_of_products_introduced_before_product_replacement',
           'price_before_replacement', 'meter_no_before_product_replacement',
           'hot_cold_classification_before_product_replacement', 'site_code',
           'department_code', 'route_code', 'customer_number', 'branch_number',
           'equipment_code', 'last_visit_date', 'last_calibration_date',
           'number_of_sales_update_failure', 'buying_place_code',
           'sales_system_representative_code', 'sales_method_detail_code',
           'in_out_classification', 'annual_contribution_sales_capacity_conversion',
           'open_closed_classification', 'contents_manufacturer_code',
           'installation_date', 'number_of_adjacent_vm_cc',
           'number_of_adjacent_vm_k', 'number_of_adjacent_vm_a',
           'number_of_adjacent_vm_dy', 'number_of_adjacent_vm_it',
           'number_of_adjacent_vm_po', 'number_of_adjacent_vm_ot',
           'number_of_adjacent_vm_sf'])
    return dataFrame

if __name__ == '__main__':
    main()
