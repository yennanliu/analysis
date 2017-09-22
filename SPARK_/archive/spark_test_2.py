
'''
ref https://databricks.com/blog/2015/08/12/from-pandas-to-apache-sparks-dataframe.html
ref https://spark.apache.org/docs/0.9.1/python-programming-guide.html
ref https://medium.com/@chris_bour/6-differences-between-pandas-and-spark-dataframes-1380cec394d2#.2vimrmb83

SPARK-csv :  https://github.com/databricks/spark-csv

'''



'''
*** RUN PYSPARK VIA  IPYTHON 
*** RUN IPYTHON WITH python 2.7  (J_env)


$source activate J_env 
$IPYTHON=1 ./bin/pyspark

'''


import pandas as pd 


# Pandas = > pdf
pdf = pd.DataFrame.from_items([('A', [1, 2, 3]), ('B', [4, 5, 6])])

type(pdf)

# SPARK SQL => df
df = sqlCtx.createDataFrame([(1, 4), (2, 5), (3, 6)], ["A", "B"])

df

type(df)

# show df in list 
df.collect()


# show df in SPARK dataframe 
df.show()


# groupby 

df.groupBy("A")
df.groupBy("A").avg("B")
df.groupBy("A").avg("B").collect()
df.groupBy("A").avg("B").show()



# adding columns 
df.withColumn('C', df.A * 2)
df.withColumn('C', df.A * 2).show()

# fliter 

df.select(df.B > 0).show()

df[(df.B > 0) & (df.A < 2)].show()


# SPARK dataframe to pandas dataframe 

pdf = df.toPandas()



# Transfer RDD to SPARK dataframe   
# (pyspark.rdd.RDD - > pyspark.sql.dataframe.DataFrame)
# ref : http://stackoverflow.com/questions/32742004/create-spark-dataframe-can-not-infer-schema-for-type-type-float

df = sc.textFile("/Users/GGV/Desktop/cs-training.csv")
df_ = df.map(lambda x: (x, )).toDF()
df_show()







