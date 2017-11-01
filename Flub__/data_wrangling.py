# python3 



import json
import pandas as pd 
import numpy as np 




def load_file():
	json_route='/Users/yennanliu/analysis/Flub__'
	with open(json_route + '/product_matching_response.json') as json_data:
		d = json.load(json_data)
		return d 

def data_preprocess():
	d = load_file()
	df_product_match = pd.DataFrame()
	# score
	need_col = [ 'score']
	for key_ in need_col:
		df_product_match[key_] = [ d['products'][k][key_] for k in range(len(d['products']))]
	# uid 
	df_product_match['uid'] = [(d['products'][k]['sources'])[0]['uid'] for k in range(len(d['products']))]
	# stock
	stock_ = []
	for k in range(len(d['products'])):
		try:
			stock_.append(d['products'][k]['merchants'][0]['stock'])
		except:
			stock_.append('NaN')
			pass
		    
	df_product_match['stock'] =  stock_
	print (df_product_match.head())
	return df_product_match




if __name__ == '__main__':
	data_preprocess()











    