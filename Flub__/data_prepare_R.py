
# python 3 
# analysis 
import pandas as pd 


def parse_csv():
	csv_route='/Users/yennanliu/analysis/Flub__'
	# only load few columns 
	# since there are potential data issues may affect column name mismatch it data 
	df_order = pd.read_csv(csv_route + '/orders.csv',usecols=["order_item_id",
	                                                          "order_id",
	                                                          "created_at",
	                                                          "order_status"])
	# fix column name 
	df_order.columns = [ 'order_id', 'created_at', 'order_status','order_item_quantity']
	print (df_order.head())
	df_order.to_csv('order_fix_.csv')
	return df_order




if __name__ == '__main__':
	parse_csv()