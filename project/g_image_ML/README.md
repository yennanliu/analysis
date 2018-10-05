### QUICK START

- Run single job 
```bash 

nohup python  run_V2.py >> run_V2.log  2>&1 

```

- Run multi job demo

```bash 
# split csv -> multi_process script run parallel job 
# run demo
python run_multi_process.py --url /Users/yennanliu/Downloads/dataset/more_duplicated_products.csv  --script test.py --process 4  --url /Users/yennanliu/Downloads/dataset/more_duplicated_products.csv
```

- Run multi job 

```bash
# split csv -> multi_process script run parallel job 
# run 
python run_multi_process.py --url /Users/yennanliu/Downloads/dataset/more_duplicated_products.csv  --script run_web_entity_parallel.py --process 4  --url /Users/yennanliu/Downloads/dataset/more_duplicated_products.csv 

```

### Ref 

- Multi-Process 
	- https://medium.com/@leportella/how-to-run-parallel-processes-8939dafae81e
	- https://maxpowerwastaken.github.io/blog/multiprocessing-with-pandas/
	- http://yaoyao.codes/python/2018/01/23/pandas-split-a-dataframe-into-chunks