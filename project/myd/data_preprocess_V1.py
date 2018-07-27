# python 3 

import pandas as pd, numpy as np



# -------------------------------


# parameter 

columns=['heart_rate', 'wrist_accelerometer_x',
'wrist_accelerometer_y', 'wrist_accelerometer_z', 'wrist_gyroscope_x',
'wrist_gyroscope_y', 'wrist_gyroscope_z', 'wrist_magnetometer_x',
'wrist_magnetometer_y', 'wrist_magnetometer_z', 'chest_accelerometer_x',
'chest_accelerometer_y', 'chest_accelerometer_z', 'chest_gyroscope_x',
'chest_gyroscope_y', 'chest_gyroscope_z', 'chest_magnetometer_x',
'chest_magnetometer_y', 'chest_magnetometer_z', 'ankle_accelerometer_x',
'ankle_accelerometer_y', 'ankle_accelerometer_z', 'ankle_gyroscope_x',
'ankle_gyroscope_y', 'ankle_gyroscope_z', 'ankle_magnetometer_x',
'ankle_magnetometer_y', 'ankle_magnetometer_z']



# -------------------------------
# help func


# op 

def load_data():
	df=pd.read_csv('imu_activity_recognition.csv')
	print (df.head())
	return df 


def get_non_null_data(df):
	# neglect heart_rate column as there are too much nan there 
	df_ = df[pd.notnull(df['wrist_accelerometer_x'])]
	df_ = df_[pd.notnull(df_['chest_accelerometer_x'])]
	df_ = df_[pd.notnull(df_['ankle_accelerometer_x'])]
	return df_ 

# feature engineering 



def get_x_y_z_sum_squre_aggregration(x,y,z):
	#print ( np.sqrt(x**2 + y**2 + z**2))
	return np.sqrt(x**2 + y**2 + z**2)



def get_x_y_z_abs_sum_aggregration(x,y,z):
	#print ( np.sqrt(x**2 + y**2 + z**2))
	return (abs(x) + abs(y)+ abs(z))


def get_direction_cosines(x,y,z):
	# http://www.geom.uiuc.edu/docs/reference/CRC-formulas/node52.html
	x_y_z_length =  np.sqrt(x**2 + y**2 + z**2)
	cos_alpha = x/x_y_z_length
	cos_beta = y/x_y_z_length
	cos_gamma = z/x_y_z_length
	return [cos_alpha, cos_beta,cos_gamma ]



def get_avg_values_(df):
	df_avg = df.groupby('activity_id').mean()
	# neglect timestamp 
	for col in columns:
		# 'wrist_accelerometer_x','wrist_accelerometer_y',...
		print ('col : ' , col)
		df_avg_ = df_avg[col].reset_index()
		df_avg_.columns = ['activity_id','avg_{}'.format(col)]
		# merge back 
		df = pd.merge(df,df_avg_,on = 'activity_id')
	return df



def get_std_values_(df):
	df_std = df.groupby('activity_id').std()
	# neglect timestamp 
	for col in columns:
		# 'wrist_accelerometer_x','wrist_accelerometer_y',...
		print ('col : ' , col)
		df_std_ = df_std[col].reset_index()
		df_std_.columns = ['activity_id','std_{}'.format(col)]
		# merge back 
		df = pd.merge(df,df_std_,on = 'activity_id')
	return df



def get_median_values_(df):
	df_median = df.groupby('activity_id').median()
	# neglect timestamp 
	for col in columns:
		# 'wrist_accelerometer_x','wrist_accelerometer_y',...
		print ('col : ' , col)
		df_median_ = df_median[col].reset_index()
		df_median_.columns = ['activity_id','median_{}'.format(col)]
		# merge back 
		df = pd.merge(df,df_median_,on = 'activity_id')
	return df


def get_max_values_(df):
	df_max = df.groupby('activity_id').max()
	# neglect timestamp 
	for col in columns:
		# 'wrist_accelerometer_x','wrist_accelerometer_y',...
		print ('col : ' , col)
		df_max_ = df_max[col].reset_index()
		df_max_.columns = ['activity_id','max_{}'.format(col)]
		# merge back 
		df = pd.merge(df,df_max_,on = 'activity_id')
	return df



def get_min_values_(df):
	df_min = df.groupby('activity_id').min()
	# neglect timestamp 
	for col in columns:
		# 'wrist_accelerometer_x','wrist_accelerometer_y',...
		print ('col : ' , col)
		df_min_ = df_min[col].reset_index()
		df_min_.columns = ['activity_id','min_{}'.format(col)]
		# merge back 
		df = pd.merge(df,df_min_,on = 'activity_id')
	return df



# -------------------------------


# ML 


# -------------------------------

def main():
	# load the data 
	df=pd.read_csv('imu_activity_recognition.csv')
	# feature extract 
	# get wrist_accelerometer in 3-D
	df['wrist_accelerometer'] = df.apply(lambda row : pd.Series(get_wrist_accelerometer(
	row['wrist_accelerometer_x'],
	row['wrist_accelerometer_y'],
	row['wrist_accelerometer_z']))
	,axis=1)
	print (df.head())
	return df 





if __name__ == '__main__':
	main()








