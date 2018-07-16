# Analytics 


## File Structure 

```bash

├── [1.4M]  EDA_r.ipynb : visualization R notebook (visualise something cool, tell a story!)
├── [1.3k]  README.md
├── [1.1k]  analysis.py : python script get outlier and average price per bedroom and bathroom
├── [3.1k]  etl.py  : ETL script to load and store the data in a Postgre
├── [2.5M]  kc_house_data.csv : house dataset
├── [ 14k]  statistical_model_nb.ipynb : ipython notebook bulid a statistical model
 
```

## Demo 
```bash
# demo of etl.py  
$ export user=<your_user>
$ export password=<your_password>
$ export host=<your_host>
$ export port=<your_port>
$ python etl.py 
load data source 
           id             date     price  bedrooms  bathrooms  sqft_living  \
0  7129300520  20141013T000000  221900.0         3       1.00         1180   
1  6414100192  20141209T000000  538000.0         3       2.25         2570   
2  5631500400  20150225T000000  180000.0         2       1.00          770   

   sqft_lot  floors  waterfront  view     ...      grade  sqft_above  \
0      5650     1.0           0     0     ...          7        1180   
1      7242     2.0           0     0     ...          7        2170   
2     10000     1.0           0     0     ...          6         770   

   sqft_basement  yr_built  yr_renovated  zipcode      lat     long  \
0              0      1955             0    98178  47.5112 -122.257   
1            400      1951          1991    98125  47.7210 -122.319   
2              0      1933             0    98028  47.7379 -122.233   

   sqft_living15  sqft_lot15  
0           1340        5650  
1           1690        7639  
2           2720        8062  

[3 rows x 21 columns]
create table OK
connect to DB
start insert data to DB


```

```bash 

# demo of analysis.py

$ python analysis.py

avg price bedroom & bathrooms : 
       price  get_avg_price_bedroom  get_avg_price_bathrooms
0   221900.0           73966.666667            221900.000000
1   538000.0          179333.333333            239111.111111
2   180000.0           90000.000000            180000.000000
3   604000.0          151000.000000            201333.333333
4   510000.0          170000.000000            255000.000000
5  1225000.0          306250.000000            272222.222222
6   257500.0           85833.333333            114444.444444
7   291850.0           97283.333333            194566.666667
8   229500.0           76500.000000            229500.000000
9   323000.0          107666.666667            129200.000000
outlier_list : 
[1651500040, 3225069065, 524059148, 3126059023, 4139910160, 2425049107, 3126059027, 7237550100, 5017000470, 6648150040, 4139420190, 8835401250, 4139910180, 4030100005, 8907500070, 2626069030, 3528000040, 3835500585, 1489300005, 404510007.....

```





