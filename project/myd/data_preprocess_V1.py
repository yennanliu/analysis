# python 3 

import pandas as pd, numpy as np



# -------------------------------

# parameter 
columns =['heart_rate', 'wrist_accelerometer_x',
'wrist_accelerometer_y', 'wrist_accelerometer_z', 'wrist_gyroscope_x',
'wrist_gyroscope_y', 'wrist_gyroscope_z', 'wrist_magnetometer_x',
'wrist_magnetometer_y', 'wrist_magnetometer_z', 'chest_accelerometer_x',
'chest_accelerometer_y', 'chest_accelerometer_z', 'chest_gyroscope_x',
'chest_gyroscope_y', 'chest_gyroscope_z', 'chest_magnetometer_x',
'chest_magnetometer_y', 'chest_magnetometer_z', 'ankle_accelerometer_x',
'ankle_accelerometer_y', 'ankle_accelerometer_z', 'ankle_gyroscope_x',
'ankle_gyroscope_y', 'ankle_gyroscope_z', 'ankle_magnetometer_x',
'ankle_magnetometer_y', 'ankle_magnetometer_z',
'wrist_accelerometer']

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

def get_wrist_accelerometer(x,y,z):
    #print ( np.sqrt(x**2 + y**2 + z**2))
    return np.sqrt(x**2 + y**2 + z**2)

def get_wrist_gyroscope():
    pass

def get_wrist_magnetometer():
    pass


def get_avg_wrist_accelerometer_x(df):
	avg_wrist_accelerometer_x = df['avg_wrist_accelerometer_x'].mean()
	return avg_wrist_accelerometer_x


def get_avg_values(df):
	for col in columns:
		print ('col : ' , col)
		temp_avg_value = df[col].mean()
		df['avg_{}'.format(col)] = temp_avg_value
	return df 


def get_median_values(df):
	for col in columns:
		print ('col : ' , col)
		temp_median_value = df[col].median()
		df['median_{}'.format(col)] = temp_avg_value
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








