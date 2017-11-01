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
	need_col = [ 'score', 'merchants', 'sources',  'identifiers']
	for key_ in need_col:
		df_product_match['key_'] = [ d['products'][k][key_] for k in range(len(d['products']))]
	# uid 
	df_product_match['uid'] = [(d['products'][k]['sources'])[0]['uid'] for k in range(len(d['products']))]
	print (df_product_match.head())
	return df_product_match






if __name__ == '__main__':
	data_preprocess()











    