
'''
ref https://databricks.com/blog/2015/08/12/from-pandas-to-apache-sparks-dataframe.html
ref https://spark.apache.org/docs/0.9.1/python-programming-guide.html

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



