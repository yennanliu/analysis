# SYSTEM DESIGN (V1)

### 1) INFRA 

```
       ETL (batch dump)
data ------------------------↓
                             ↓
			 ETL ↓
		       <---> ↓     (train results)
Redshift (DW, for EDA) <---- S3 <-------↑
			   ↑ ↓ ↓        ↑
			   ↑ ↓ ↓-------> SageMaker (ML train/deploy)
		       ETL ↑ ↓ 
		           ↑ ↓
			  EMR (ML dev, ETL dev)
			  (spark, hadoop, hive)

```

### 2) MAIN COMPONENTS 

### 3) S3 BUCKET 

### 4) EMR 

### 5) Redshift

### 6) SageMaker
