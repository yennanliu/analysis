'''

SPARK TEST 20160630

ref :  https://www.codementor.io/spark/tutorial/python-spark-sql-dataframes
ref :  https://spark.apache.org/docs/latest/sql-programming-guide.html#creating-dataframes
ref :  https://github.com/jadianes/spark-py-notebooks/blob/master/nb2-rdd-basics/nb2-rdd-basics.ipynb

visit sparkUI via http://192.168.0.91:4041

'''

source activate spark ; cd ; cd spark ; ./bin/pyspark

from pyspark.sql import SQLContext
from pyspark.sql.types import *
sqlContext = SQLContext(sc)



###  read CSV

# method 1 
sc.textFile("/Users/GGV/Desktop/test.csv").collect()
df = sc.textFile("/Users/GGV/Desktop/test.csv")
df.count()

###  read CSV and to DataFrame

sc.textFile("/Users/GGV/Desktop/test.csv").collect()
df = sc.textFile("/Users/GGV/Desktop/test.csv")
df_data = df.map(lambda l: l.split(","))
df_row_data = df_data.map(lambda p: Row(
    PassengerId=(p[0]), Pclass=p[1],Name=p[2],Sex=p[3],Age=p[4],SibSp=(p[5]),Parch=(p[6]),
    Ticket=(p[7]),Fare=(p[8]),Cabin=(p[9]),Embarked=(p[10]))
)
interactions_df = sqlContext.createDataFrame(df_row_data)
interactions_df.registerTempTable("test")
tcp_test = sqlContext.sql(""" SELECT * FROM test """)
tcp_test.show()

interactions_df.printSchema()



###   read CSV and to DataFrame pt.2


import urllib
f = urllib.urlretrieve ("http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data_10_percent.gz", "kddcup.data_10_percent.gz")


# get data from file
data_file = "./kddcup.data_10_percent.gz"
raw_data = sc.textFile(data_file)

# parse into key-value pairs
key_csv_data = raw_data.map(parse_interaction)

# filter normal key interactions
normal_key_interactions = key_csv_data.filter(lambda x: x[0] == "normal.")

# collect all
t0 = time()
all_normal = normal_key_interactions.collect()
tt = time() - t0
normal_count = len(all_normal)
print "Data collected in {} seconds".format(round(tt,3))
print "There are {} 'normal' interactions".format(normal_count)


















