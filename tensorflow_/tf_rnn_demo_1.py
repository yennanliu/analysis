"""
modify from  
https://github.com/chentinghao/tinghao-tensorflow-rnn-tutorial

"""

import tensorflow as tf
import numpy as np

def reset_graph(seed=777):
    tf.reset_default_graph()
    tf.set_random_seed(seed)
    np.random.seed(seed)






# ------------------------ build RNN with static_rnn  ------------------------
print ('# ------------------------ build RNN with static_rnn  ------------------------')
# reset
reset_graph()

# input data
X_data = np.array([
# steps   1st     2nd       3rd
        [[1, 2], [7, 8], [13, 14]],  # first batch
        [[3, 4], [9, 10], [15, 16]], # second batch
        [[5, 6], [11, 12], [17, 18]] # third batch
]) # shape: [batch_size, n_steps, n_inputs]
# hyperparameters
n_neurons = 8

# parameters
n_inputs = X_data.shape[2]
n_steps = X_data.shape[1]

# rnn model
X = tf.placeholder(tf.float32, [None, n_steps, n_inputs])
X_seq = tf.unstack(X, axis=1) # shape: [batch_size, i, n_inputs], total num of i = n_steps

cell = tf.nn.rnn_cell.BasicRNNCell(num_units=n_neurons)
output, state = tf.nn.static_rnn(cell, X_seq, dtype=tf.float32)

output_st = tf.stack(output, axis=1)
# initialize the variables
init = tf.global_variables_initializer()

# train
with tf.Session() as sess:
    sess.run(init)
    feed_dict = {X: X_data}
    
    # print the shape
    X_seq_shape = sess.run(tf.shape(X_seq), feed_dict=feed_dict)
    output_shape = sess.run(tf.shape(output), feed_dict=feed_dict)
    state_shape = sess.run(tf.shape(state), feed_dict=feed_dict)
    output_st_shape = sess.run(tf.shape(output_st), feed_dict=feed_dict)
    print (' ---------------------- outout  ----------------------')
    print ('* input : ')
    print (X_data)
    print('* X_seq shape [batch_size, n_steps, n_inputs]: ', X_seq_shape)
    print('* output shape [batch_size, n_neurons]: ', output_shape)
    print('* state shape [batch_size, n_neurons]: ', state_shape)
    print('* output_st shape [batch_size, n_steps, n_neurons]: ', output_st_shape)
    output_eval, state_eval = sess.run([output, state], feed_dict=feed_dict)



# ------------------------ build RNN with dynamic_rnn  ------------------------
print ('# ------------------------ build RNN with dynamic_rnn  ------------------------')


# reset
reset_graph()

# input data
X_data = np.array([
# steps   1st     2nd       3rd
        [[1, 2], [7, 8], [13, 14]],  # first batch
        [[3, 4], [9, 10], [15, 16]], # second batch
        [[5, 6], [11, 12], [17, 18]] # third batch
]) # shape: [batch_size, n_steps, n_inputs]
# hyperparameters
n_neurons = 8

# parameters
n_inputs = X_data.shape[2]
n_steps = X_data.shape[1]

# rnn model
### different from static_rnn 
X = tf.placeholder(tf.float32, [None, n_steps, n_inputs])

cell = tf.nn.rnn_cell.BasicRNNCell(num_units=n_neurons)
### different from static_rnn 
output, state = tf.nn.dynamic_rnn(cell, X, dtype=tf.float32)

# initialize the variables
init = tf.global_variables_initializer()

# train
with tf.Session() as sess:
    sess.run(init)
    feed_dict = {X: X_data}
    
    # print the shape
    output_shape = sess.run(tf.shape(output), feed_dict=feed_dict)
    state_shape = sess.run(tf.shape(state), feed_dict=feed_dict)
    print (' ---------------------- outout  ----------------------')
    print ('* input : ')
    print (X_data)
    print('* X_seq shape [batch_size, n_steps, n_inputs]: ', X_seq_shape)
    print('* output shape [batch_size, n_neurons]: ', output_shape)
    print('* state shape [batch_size, n_neurons]: ', state_shape)
    print('* output_st shape [batch_size, n_steps, n_neurons]: ', output_st_shape)
    output_eval, state_eval = sess.run([output, state], feed_dict=feed_dict)







# ------------------------ build  multi RNN cell  ------------------------
print ('# ------------------------ build  multi RNN cell  ------------------------')


# reset
reset_graph()

# input data
X_data = np.array([
# steps   1st     2nd       3rd
        [[1, 2], [7, 8], [13, 14]],  # first batch
        [[3, 4], [9, 10], [15, 16]], # second batch
        [[5, 6], [11, 12], [17, 18]] # third batch
]) # shape: [batch_size, n_steps, n_inputs]
# hyperparameters
n_neurons = 8


# hyperparameters
n_neurons = 8

# parameters
n_steps = X_data.shape[1]
n_inputs = X_data.shape[2]
n_layers = 10 # 10 hidden layers

# rnn model
X = tf.placeholder(tf.float32, [None, n_steps, n_inputs])

layers = [tf.nn.rnn_cell.BasicRNNCell(num_units=n_neurons) for _ in range(n_layers)]
multi_rnn = tf.nn.rnn_cell.MultiRNNCell(layers)
output, state = tf.nn.dynamic_rnn(multi_rnn, X, dtype=tf.float32)


# initializer the variables
init = tf.global_variables_initializer()

# train
with tf.Session() as sess:
    sess.run(init)
    feed_dict = {X: X_data}
    output_shape = sess.run(tf.shape(output), feed_dict=feed_dict)
    state_shape = sess.run(tf.shape(state), feed_dict=feed_dict)
    print (' ---------------------- outout  ----------------------')
    print ('* input : ')
    print (X_data)
    print('* X_seq shape [batch_size, n_steps, n_inputs]: ', X_seq_shape)
    print('* output shape [batch_size, n_neurons]: ', output_shape)
    print('* state shape [batch_size, n_neurons]: ', state_shape)
    print('* output_st shape [batch_size, n_steps, n_neurons]: ', output_st_shape)
    output_eval, state_eval = sess.run([output, state], feed_dict=feed_dict)






