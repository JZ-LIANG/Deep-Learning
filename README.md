# Deep Learning
This repository contains my project notebooks for the Deep Learning course at EURECOM.

***

## Notebooks
### [LAB1_FCNN](https://github.com/JZ-LIANG/Deep-Learning/blob/master/LAB1_FCNN/LAB1_FCNN.ipynb)
* Implement a Two Layers Fully Connected Neural Network in **Numpy** by hand writing the Feedforward and Backpropagation functions.  
* Train and evaluate models on MNIST data set, Comparing the influences of:
	 * Stochastic / Batch / Mini batch gradient descent
	 * different hidden layer size
	 * different learning rate
	 * sigmoid / softmax output


### [LAB2_CNN](https://github.com/JZ-LIANG/Deep-Learning/blob/master/LAB2_CNN/LAB2_CNN.ipynb)

<img align="right" src="https://github.com/JZ-LIANG/Deep-Learning/blob/master/LAB2_CNN/images/LeNet.png" width="250">

* Using **Tensorboard** to visualize the graph and training progress.
* Re-build the FCNN model using **Tensorflow**.
* Implement a LeNet-5 CNN model in **Tensorflow**
* Perform some optimizations to get more than **99%** of accuracy on MNIST.
 * Different Optimizer :Gradient Descent vs AdamOptimizer
 * Dropout





### [LAB3_RNN](https://github.com/JZ-LIANG/Deep-Learning/blob/master/LAB3_RNN/LAB3_RNN.ipynb)

<img align="right" src="https://github.com/JZ-LIANG/Deep-Learning/blob/master/LAB3_RNN/images/GRU.png" width="250">

* Build a Vanilla-RNN and a GRU by hand writing the formulas in **Tensorflow**.
* Classify user comments  from IMDb, Amazon, and Yelp to two classification(Negative / Positive).
