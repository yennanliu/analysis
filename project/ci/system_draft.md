### system design (V1)

### infra 

```

data ------------------------↓
                             ↓
			     ↓
			     ↓     (train results)
Redshift (DW, for EDA) <---- S3 <-------↑
			     ↓ ↓        ↑
			     ↓ ↓-------> SageMaker (model train, deploy)
			     ↓ 
		             ↓
			    EMR (dev env)

```
