# SYSTEM DESIGN (V1)

### 1) INFRA 

```
       ETL (batch dump)
data ------------------------↓
                             ↓
			     ↓
		  ↓----------↓    
		  ↓          
                  ↓↑ ------> Redshift 
		  ↓↑	     (DW,master data)             
		  S3           ↑ ↓ ↓                (train results)
		  ↓ ↑ <--------- ↓ ↓ --------------------↑
		  ↓ <--------- ↑ ↓ ↓                     ↑
            Athena  <------- ↑ ↑ ↓        	         ↑
          (ad-hoc)           ↑ ↑ ↓---------------> SageMaker
		           ETL ↑ ↓                    (ML train/deploy)
		               ↑ ↓
		               ↑ ↓
		               ↑ ↓
		               ↑ ↓
			       EMR 
			       (ML dev, ETL dev)
			       (spark, hadoop, hive)

```

### 2) MAIN COMPONENTS 

* Data storage
 -Data lake
 -Database 
 -Data warehouse 
* ETL
   - EMR
* ML
   - SageMaker

### 3) S3 BUCKET 

### 4) EMR 

### 5) Redshift

### 6) SageMaker
