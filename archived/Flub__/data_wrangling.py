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
			stock_.append(float('nan'))
			pass
		    
	df_product_match['stock'] =  stock_
	# fix type 
	df_product_match.score = df_product_match.score.convert_objects(convert_numeric=True)
	df_product_match.stock = df_product_match.stock.convert_objects(convert_numeric=True)
	# show the data 
	print (df_product_match.head())
	return df_product_match


def analysis():
	df_product_match = data_preprocess()
	print ('')
	print ('1)  General Situation --------------')
	# all
	print ('all data counts : ', len(df_product_match))

	# accepted 
	print ('accepted data counts : ', len(df_product_match[df_product_match.score > 0.5]))

	# rejected
	print ('rejected data counts : ', len(df_product_match[df_product_match.score < 0.02]))

	# should be checked by agents
	print ('should be checked by agents data counts : ', len(df_product_match[(df_product_match.score <= 0.5)
	                            & (df_product_match.score >= 0.02) ]))
	print ('')
	print ('')
	print ('2) Considering only the accepted products --------------')
	print ('accepted & in stock product : ',len(df_product_match[(df_product_match.score > 0.5)
                 & (df_product_match.stock > 0)]))
 



if __name__ == '__main__':
	analysis()











    