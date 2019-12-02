#!/bin/sh
####################################################################
# SCRIPT BUILD AGGREGRATED MONTH TRANSACTION TABLE
####################################################################


build_month_aggr_trans() {
    base_sql="""

      WITH filtered_vm AS
        (SELECT sales_date,
                branch_number,
                customer_number,
                equipment_code,
                count(DISTINCT product_code)::numeric/max(column_no)::numeric AS item_ratio
         FROM target_vm_9000_vm_transaction_
         GROUP BY 1,
                  2,
                  3,
                  4
         HAVING item_ratio > 0.5),
           filtered_t AS
        (SELECT *
         FROM target_vm_9000_vm_transaction_
         WHERE (sales_date,
                branch_number,
                customer_number,
                equipment_code) IN
             (SELECT sales_date,
                     branch_number,
                     customer_number,
                     equipment_code
              FROM filtered_vm) ),
           aggre_t AS
        (SELECT SUBSTRING(sales_date, 1, 7) AS sales_month,
                branch_number,
                customer_number,
                equipment_code,
                column_no,
                product_code,
                site_code,
                department_code,
                route_code,
                customer_number,
                group_company_code,
                selling_price,
                meter_no,
                hot_cold_classification,
                buying_place_code,
                sales_system_representative_code,
                sales_method_detail_code,
                in_out_classification,
                annual_contribution_sales_capacity_conversion,
                open_closed_classification,
                contents_manufacturer_code,
                installation_date,
                product_code_before_replacement,
                hot_cold_classification_before_product_replacement AS hot_cold_classification_before_replacement,
                number_of_sales_update_failure,
                number_of_adjacent_vm_cc,
                number_of_adjacent_vm_k,
                number_of_adjacent_vm_a,
                number_of_adjacent_vm_dy,
                number_of_adjacent_vm_it,
                number_of_adjacent_vm_po,
                number_of_adjacent_vm_ot,
                number_of_adjacent_vm_sf,
                sum(sales_quantity) AS sales_quantity
         FROM filtered_t
         WHERE number_of_sales_update_failure = 0
           AND sales_quantity < 1000
         GROUP BY 1,
                  2,
                  3,
                  4,
                  5,
                  6,
                  7,
                  8,
                  9,
                  10,
                  11,
                  12,
                  13,
                  14,
                  15,
                  16,
                  17,
                  18,
                  19,
                  20,
                  21,
                  22,
                  23,
                  24,
                  25,
                  26,
                  27,
                  28,
                  29,
                  30,
                  31,
                  32,
                  33)
      SELECT *
      FROM aggre_t;
       """
    for i in 201901 201902 201903
        do
            SQL=$(echo $base_sql | sed -e "s/\target_vm_9000_vm_transaction_/target_vm_9000_vm_transaction_$i/g")
            echo $SQL
            echo --------
        done 
}

run_sql_with_args(){

base_sql="select 1;"
psql -d "host=$host port=$port dbname=$dbname user=$user" \
    --command="select 1;"
}

# init your creds
#export PGPASSWORD=<PGPASSWORD>
#export connection_string="host=xxxxx.amazonaws.com port=5439 dbname=dbname user=user"
#build_month_aggr_trans
run_sql_with_args
