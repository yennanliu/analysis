# python 3 

# analytics 
import pandas as pd, numpy as np
from scipy import stats

from data_prepare import *



def get_data():

	df = load_data()
	df_ = data_preprocess(df)
	df_ = order_value_feature(df_)
	df_ = time_feature(df_)
	df_ = label_feature(df_)
	df_train = finalize_user_profile(df_)
	df_train['order_again_'] = df_train.order_count.apply(lambda x : order_again(x))
	return df_train, df_


############## Using two sample t test to test if data is data segments are Outperforming/underperforming #############
def stats_comparison_(i):
	df_train, df_ = get_data()

	df_train.groupby(i)['order_again_']\
			.agg({'average': 'mean','order_again': 'count'})\
			.reset_index()


	cat = df_train.groupby(i)['order_again_']\
				.agg({'sub_average': 'mean','sub_order_again': 'count'})\
				.reset_index()
	cat['overall_average'] = df_train['order_again_'].mean()
	cat['overall_order_again'] = df_train['order_again_'].count()
	cat['rest_order_again'] = cat['overall_order_again'] - cat['sub_order_again']
	cat['rest_average'] = (cat['overall_order_again']*cat['overall_average'] \
							- cat['sub_order_again']*cat['sub_average'])/cat['rest_order_again']
	cat['z_score'] = (cat['sub_average']-cat['rest_average'])/\
					np.sqrt(cat['overall_average']*(1-cat['overall_average'])
					*(1/cat['sub_order_again']+1/cat['rest_order_again']))
	cat['prob'] = np.around(stats.norm.cdf(cat.z_score), decimals = 10)
	cat['significant'] = [(lambda x: 1 if x > 0.9 else -1 if x < 0.1 else 0)(i) for i in cat['prob']]

	print (cat)







stats_comparison_('platform_')




