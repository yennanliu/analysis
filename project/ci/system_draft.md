### 1) SYSTEM DESIGN (V1)

### 2) INFRA 

```

data ------------------------↓
                             ↓
			     ↓
			     ↓     (train results)
Redshift (DW, for EDA) <---- S3 <-------↑
			   ↑ ↓ ↓        ↑
			   ↑ ↓ ↓-------> SageMaker (model train, deploy)
		      ETl  ↑ ↓ 
		           ↑ ↓
			    EMR (dev env)

```

### 3) MAIN COMPONENTS 

### 4) S3 BUCKET 

### 5) EMR 

### 6) Redshift

### 7) SageMaker
