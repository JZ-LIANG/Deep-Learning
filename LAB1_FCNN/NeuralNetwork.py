import time
import random
import numpy as np
from utils import *
from transfer_functions import * 
import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')

class NeuralNetwork(object):
    
    def __init__(self, 
                 input_layer_size, 
                 hidden_layer_size, 
                 output_layer_size, 
                 transfer_f=sigmoid, 
                 transfer_df=dsigmoid):
        """
        input_layer_size: number of input neurons
        hidden_layer_size: number of hidden neurons
        output_layer_size: number of output neurons
        iterations: number of iterations
        learning_rate: initial learning rate
        """

        # initialize transfer functions
        self.transfer_f = transfer_f
        self.transfer_df = transfer_df

        # initialize layer sizes
        self.input_layer_size = input_layer_size+1  # +1 for the bias node in the input Layer
        self.hidden_layer_size = hidden_layer_size+1 # +1 for the bias node in the hidden layer 
        self.output_layer_size = output_layer_size

        # initialize arrays for activations
        self.u_hidden = np.zeros(self.hidden_layer_size-1)
        self.u_output = np.zeros(self.output_layer_size)

        # initialize arrays for outputs
        self.o_input = np.ones(self.input_layer_size)
        self.o_hidden = np.ones(self.hidden_layer_size)
        self.o_output = np.ones(self.output_layer_size)

        # initialize arrays for partial derivatives according to activations
        self.dE_du_hidden = np.zeros(self.hidden_layer_size-1)
        self.dE_du_output = np.zeros(self.output_layer_size)

        # create randomized weights Yann LeCun method in 1988's paper (Default values)
        self.initialize_weights()

    def initialize_weights(self, wi=None, wo=None):
        input_range = 1.0 / self.input_layer_size ** (1/2)
        
        # initialize weights between input and hidden layer
        if wi is not None:
            self.W_input_to_hidden = wi
        else:
            self.W_input_to_hidden = np.random.normal(loc = 0, 
                                                      scale = input_range, 
                                                      size = (self.input_layer_size, 
                                                              self.hidden_layer_size-1))
            
        # initialize weights between hidden and output layer
        if wo is not None:
            self.W_hidden_to_output = wo
        else:
            self.W_hidden_to_output = np.random.uniform(size = (self.hidden_layer_size, 
                                                                self.output_layer_size)
                                                       ) / np.sqrt(self.hidden_layer_size)       

    def accuracy(self, test_data,sm_xe):
        """ Returns percentage of well classified samples """
            
        # compute the predictions
        self.feedforward(test_data[0],sm_xe)
            
        # count correct predictions
        target = np.argmax(test_data[1], axis=1)
        prediction = np.argmax(self.o_output, axis=1)
        count = np.sum(target == prediction)
                
        return count * 100 / len(test_data[0])
    
    def plot_curves(self, train_accuracies, val_accuracies, errors, learning_rate, best_acc_it):

        # get x axis
        iterations = np.arange(len(train_accuracies))
        
        _, ax = plt.subplots(1, 2, figsize=(13, 4))
        
        # plot accuracies curve
        ax[0].plot(iterations, train_accuracies, label="Training data", color="blue")
        ax[0].plot(iterations, val_accuracies, label="Validation data", color="orange")
        best_accuracy = val_accuracies[best_acc_it]
        ax[0].plot([0, best_acc_it, best_acc_it], [best_accuracy, best_accuracy, 0], color="green", ls="--", alpha=0.6, label="Best accuracy")
        ax[0].legend()
        # ax[0].grid()
        ax[0].set_title("Accuracy learning curve")
        ax[0].set_xlabel("Epochs")
        ax[0].set_ylabel("Accuracy [%]")
        
        # plot MSE curve
        ax[1].plot(iterations, errors, label="Mean Squared Error")
        ax[1].legend()
        # ax[1].grid()
        ax[1].axhline(y=0, color="red", ls="--")
        ax[1].set_title("Mean Squared Error learning curve")
        ax[1].set_xlabel("Epochs")
        ax[1].set_ylabel("MSE")
        
        plt.suptitle('Hidden Layer Size: {} - Learning Rate: {} - Accuracy: {} %'.format(self.hidden_layer_size-1, learning_rate, best_accuracy))
        plt.show() 
                       
   
