### QUICK START

- Run single job 
```bash 

nohup python  run_V2.py >> run_V2.log  2>&1 

```

- Run parallel job 
```bash 

python split_csv.py --url /Users/yennanliu/Downloads/dataset/demo.csv --chunk_size 10

```

### Ref 

- Multi-Process 
	- https://medium.com/@leportella/how-to-run-parallel-processes-8939dafae81e
	- https://maxpowerwastaken.github.io/blog/multiprocessing-with-pandas/
	- http://yaoyao.codes/python/2018/01/23/pandas-split-a-dataframe-into-chunks