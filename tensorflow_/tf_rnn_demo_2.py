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

Y_data = np.array([
# steps   1st     2nd       3rd
        [[1]],  # first batch
        [[0]], # second batch
        [[1]] # third batch
        ]) # shape: [batch_size, n_steps, n_inputs]


# hyperparameters
n_neurons = 20
learning_rate = 0.0001
batch_size = 64
n_epochs = 20

# parameters
n_steps = 3 # 3 rows
n_inputs = 3 # 3 cols
n_outputs = 2 # 2 classes

# parameters
#n_inputs = X_data.shape[2]
#n_steps = X_data.shape[1]



# rnn model
### different from static_rnn 
X = tf.placeholder(tf.float32, [None, n_steps, n_inputs])
y = tf.placeholder(tf.float32, [None])



cell = tf.nn.rnn_cell.BasicRNNCell(num_units=n_neurons)
### different from static_rnn 
output, state = tf.nn.dynamic_rnn(cell, X, dtype=tf.float32)
logits = tf.layers.dense(state, n_outputs)
cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=y, logits=logits)
loss = tf.reduce_mean(cross_entropy)
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(loss)
prediction = tf.nn.in_top_k(logits, y, 1)
accuracy = tf.reduce_mean(tf.cast(prediction, tf.float32))



# initialize the variables
init = tf.global_variables_initializer()

##### train the model
sess = tf.Session()
sess.run(init)
n_batches = n_steps // batch_size
loss_list = []
acc_list = []
for epoch in range(n_epochs):
    for batch in range(n_batches):
        X_train, y_train = list(zip(X_data,Y_data))[batch][0], list(zip(X_data,Y_data))[batch][1]
        X_train = X_train.reshape([-1, n_steps, n_inputs])
        sess.run(optimizer, feed_dict={X: X_train, y: y_train})
    loss_train, acc_train = sess.run(
        [loss, accuracy], feed_dict={X: X_train, y: y_train})
    loss_list.append(loss_train)
    acc_list.append(acc_train)
    print('Epoch: {}, Train Loss: {:.3f}, Train Acc: {:.3f}'.format(
        epoch + 1, loss_train, acc_train))
loss_test, acc_test = sess.run(
    [loss, accuracy], feed_dict={X: X_test, y: y_test})
print('Test Loss: {:.3f}, Test Acc: {:.3f}'.format(loss_test, acc_test))




# ------------------------ build  multi RNN cell  ------------------------
print ('# ------------------------ build  multi RNN cell  ------------------------')





