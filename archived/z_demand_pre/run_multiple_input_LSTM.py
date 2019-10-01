# ref 
# https://stackoverflow.com/questions/42532386/how-to-work-with-multiple-inputs-for-lstm-in-keras

# ops 
import numpy
import pandas
import math
# ML 
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error



# help function 
# -------------------
def create_dataset(dataset, look_back=1):
    dataX, dataY = [], []
    # modify look_back is possible 
    for i in range(len(dataset) - look_back - 1):
        a = dataset[i:(i + look_back), :]
        dataX.append(a)
        """ get the predict column : 
        	dataset[i + look_back, 4]
        	(is the 4th column in this dataset)
        """
        dataY.append(dataset[i + look_back, 4])
    return numpy.array(dataX), numpy.array(dataY)



def filter_col(df):
	cols = ['Open', 'High', 'Low','Volume', 'Close']
	df_ = df[cols]
	return df_ 


def get_data():
	dataframe = pandas.read_csv('table.csv', engine='python')
	dataframe_ = filter_col(dataframe)
	dataset = dataframe_.values
	return  dataframe_, dataset

def prepare_data(dataset):
	# normalize the dataset
	scaler = MinMaxScaler(feature_range=(0, 1))
	dataset = scaler.fit_transform(dataset)
	# split into train and test sets
	# todo : do this randomly  
	train_size = int(len(dataset) * 0.67) 
	test_size = len(dataset) - train_size
	train, test = dataset[0:train_size, :], dataset[train_size:len(dataset), :]
	# reshape into X=t and Y=t+1
	look_back = 3
	trainX, trainY = create_dataset(train, look_back)  
	testX, testY = create_dataset(test, look_back)
	# reshape dataset 
	trainX = numpy.reshape(trainX, (trainX.shape[0], look_back, 5))
	testX = numpy.reshape(testX, (testX.shape[0],look_back, 5))
	return trainX, trainY, testX, testY



# -------------------





if __name__ == '__main__':
	# -------------------
	# get data 
	dataframe_, dataset = get_data()
	trainX, trainY, testX, testY = prepare_data()
	# -------------------
	# build and run the model 
	model = Sequential()
	### need to modify here ###
	### look_back = 3 -> 5 ( dim of cols)
	#model.add(LSTM(4, input_dim=look_back))
	model.add(LSTM(4, input_dim=5))


	model.add(Dense(1))
	model.compile(loss='mean_squared_error', optimizer='adam')
	history= model.fit(trainX, trainY,validation_split=0.33, nb_epoch=20, batch_size=32)


	# make predictions
	trainPredict = model.predict(trainX)
	testPredict = model.predict(testX)

	# Get something which has as many features as dataset
	trainPredict_extended = numpy.zeros((len(trainPredict),5))
	# Put the predictions there
	trainPredict_extended[:,5] = trainPredict[:,0]

	# Inverse transform it and select the 5rd column.
	#trainPredict = scaler.inverse_transform(trainPredict_extended) [:,2]  
	trainPredict = scaler.inverse_transform(trainPredict_extended) [:,5]

	print(trainPredict)
	# Get something which has as many features as dataset
	testPredict_extended = numpy.zeros((len(testPredict),5))
	# Put the predictions there
	testPredict_extended[:,5] = testPredict[:,0]
	# Inverse transform it and select the 5rd column.
	testPredict = scaler.inverse_transform(testPredict_extended)[:,5]   


	trainY_extended = numpy.zeros((len(trainY),3))
	trainY_extended[:,2]=trainY
	trainY=scaler.inverse_transform(trainY_extended)[:,2]


	testY_extended = numpy.zeros((len(testY),3))
	testY_extended[:,2]=testY
	testY=scaler.inverse_transform(testY_extended)[:,2]


	# calculate root mean squared error
	trainScore = math.sqrt(mean_squared_error(trainY, trainPredict))
	print('Train Score: %.2f RMSE' % (trainScore))
	testScore = math.sqrt(mean_squared_error(testY, testPredict))
	print('Test Score: %.2f RMSE' % (testScore))

	# shift train predictions for plotting
	trainPredictPlot = numpy.empty_like(dataset)
	trainPredictPlot[:, :] = numpy.nan
	trainPredictPlot[look_back:len(trainPredict)+look_back, 2] = trainPredict

	# shift test predictions for plotting
	testPredictPlot = numpy.empty_like(dataset)
	testPredictPlot[:, :] = numpy.nan
	testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, 2] = testPredict







