import numpy as np
import time
from keras.datasets import mnist
import numpy as np
import lowpy as lp

# Start timer from 0
def tic():
    global t
    t = time.time()

# Lap timer
def toc():
    global t
    print(time.time() - t)


#-----IMPORT DATASET-----#
(trainData, trainLabels), (testData, testLabels) = mnist.load_data()
trainData   = np.float64(trainData.reshape( trainData.shape[0], trainData.shape[1]*trainData.shape[2]   )) # Reshape train data from [n,28,28] to [n,784]
trainLabels = np.int32(trainLabels)
testData    = np.float64(testData.reshape(  testData.shape[0],  testData.shape[1]*testData.shape[2]     )) # Reshape test data from [n,28,28] to [n,784]
testLabels  = np.int32(testLabels)
#-----NORMALIZE DATA-----#
trainData   = np.true_divide(trainData, max(np.max(trainData), np.max(testData)))
testData    = np.true_divide(testData,  max(np.max(trainData), np.max(testData)))
history = []
#----GLOBAL PARAMETERS---#
number_of_networks      = 10
input_shape             = 784
alpha                   = [ 0.1,    0.1,    0.1,    0.1,    0.1,    0.1,    0.1,    0.1,    0.1,    0.1]
beta                    = np.zeros(number_of_networks)
sigma_i                 = [ 0.5,    0.1,    0.05,   0.01,   0.005,  0.001,  0.0005, 0.0001, 0.00005,0.00001]
weight_initialization   = "uniform"
#--SIMULATION PARAMETERS-#
epochs = 10
batch_size = 60000
tests_per_epoch = 5
validation_data = (testData,testLabels)
verbose = True

model = lp.Sequential(number_of_networks=number_of_networks)
# Build Model
model.add(  
    lp.Dense(   
        10,    
        input_shape=input_shape,    
        alpha=alpha,    
        beta=beta,     
        weight_initialization=weight_initialization, 
        sigma_i=sigma_i   
    )
)
# model.add(  
#     lp.Dense(   
#         10,      
#         alpha=alpha,    
#         beta=beta,     
#         weight_initialization=weight_initialization, 
#         sigma_i=sigma_i   
#     )
# )
# Simulate Model
history = model.fit(
    trainData, 
    trainLabels, 
    epochs=epochs, 
    batch_size=batch_size, 
    tests_per_epoch=tests_per_epoch, 
    validation_data=(testData, testLabels), 
    verbose=True
)