### SYSTEM DESIGN (V1)

### INFRA 

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

### MAIN COMPONENTS 

### S3 BUCKET 

### EMR 

### Redshift

### SageMaker
