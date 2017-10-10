import pandas as pd, numpy as np


from prepare import *




if __name__ == '__main__':
	
	df = load_data()
	df_ = data_preprocess(df)
	df_ = order_value_feature(df_)
	df_ = time_feature(df_)
	df_ = label_feature(df_)
	df_train = finalize_user_profile(df_)
