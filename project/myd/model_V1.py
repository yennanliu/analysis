# python 3 

import pandas as pd, numpy as np

# help func

# -------------------------------


# op 


# feature engineering 

def get_wrist_accelerometer(x,y,z):
    #print ( np.sqrt(x**2 + y**2 + z**2))
    return np.sqrt(x**2 + y**2 + z**2)

def get_wrist_gyroscope():
    pass

def get_wrist_magnetometer():
    pass


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








