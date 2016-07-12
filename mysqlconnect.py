import pymysql
from pymysql import * 


conn= pymysql.connect(host=dburl,port = 3306,user='root',password=password,db='mysqltest1',cursorclass=pymysql.cursors.DictCursor)
a=conn.cursor()
sql='select * from taxi limit 10 ; '
a.execute(sql)

for k in a:
	print (k)
