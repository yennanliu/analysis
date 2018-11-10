# python 3 

#########################################################
#
# HELP FUNC FOR SETTING UP TENSORFLOW DL MODEL
#########################################################

# OP 
import numpy as np
import pandas as pd 

# DL 
import tensorflow as tf




def get_next_batch_V1(X_train,Y_train):
	"""	
	# get batch X, y data 
	# https://stackoverflow.com/questions/44565186/how-to-implement-next-batch-function-for-custom-data-in-python			
	"""
    idxs = np.random.permutation(X_train.shape[0]) #shuffled ordering
    X_random_batch  = X_train[idxs]
    Y_random_batch = Y_train[idxs]
    return X_random_batch,  Y_random_batch



def batch_generator(batch_size, sequence_length):
    """  
    Generator function for creating random batches of training-data.
    plz check  mnist.train.next_batch(batch_size) for ideas 
    # https://github.com/tensorflow/tensorflow/blob/master/tensorflow/contrib/learn/python/learn/datasets/mnist.py#L183  
    """
    # Infinite loop.
    while True:
        # Allocate a new array for the batch of input-signals.
        x_shape = (batch_size, sequence_length, num_x_signals)
        x_batch = np.zeros(shape=x_shape, dtype=np.float16)

        # Allocate a new array for the batch of output-signals.
        y_shape = (batch_size, sequence_length, num_y_signals)
        y_batch = np.zeros(shape=y_shape, dtype=np.float16)

        # Fill the batch with random sequences of data.
        for i in range(batch_size):
            # Get a random start-index.
            # This points somewhere into the training-data.
            idx = np.random.randint(num_train - sequence_length)
            
            # Copy the sequences of data starting at this index.
            x_batch[i] = x_train_scaled[idx:idx+sequence_length]
            y_batch[i] = y_train_scaled[idx:idx+sequence_length]
        
        yield (x_batch, y_batch)


