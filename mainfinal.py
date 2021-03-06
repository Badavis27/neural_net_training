
from __future__ import division
import neuro
import linear_algebra
import sys
import numpy as np

#training inputs and there targets 
inputs = [ [0.2,0.0,0.0],  [0.4,0.0,0.0],  [0.6,0.0,0.0],  [0.8,0.0,0.0],  [1.0,0.0,0.0],  [1.0,0.2,0.2],  [1.0,0.4,0.4],  [1.0,0.6,0.6],  [1.0,0.8,0.8],
		   [0.2,0.09,0.0], [0.4,0.2,0.0],  [0.6,0.29,0.0], [0.8,0.4,0.0],  [1.0,0.5,0.0],  [1.0,0.6,0.2],  [1.0,0.69,0.4], [1.0,0.8,0.6],  [1.0,0.89,0.8],
		   [0.2,0.2,0.0],  [0.4,0.4,0.0],  [0.6,0.6,0.0],  [0.8,0.8,0.0],
		   [0.09,0.2,0.0], [0.2,0.4,0.0],  [0.29,0.6,0.0], [0.4,0.8,0.0],  [0.5,1.0,0.0],  [0.6,1.0,0.2],  [0.69,1.0,0.4], [0.8,1.0,0.6],  [0.89,1.0,0.8],
		   [0.0,0.2,0.0],  [0.0,0.4,0.0],  [0.0,0.6,0.0],  [0.0,0.8,0.0],  [0.0,1.0,0.0],  [0.2,1.0,0.2],  [0.4,1.0,0.4],  [0.6,1.0,0.6],  [0.8,1.0,0.8],
		   [0.0,0.2,0.09], [0.0,0.4,0.2],  [0.0,0.6,0.29], [0.0,0.8,0.4],  [0.0,1.0,0.5],  [0.2,1.0,0.6],  [0.4,1.0,0.69], [0.6,1.0,0.8],  [0.8,1.0,0.89],
		   [0.0,0.2,0.2],  [0.0,0.4,0.4],  [0.0,0.6,0.6],  [0.0,0.8,0.8],  [0.0,1.0,1.0],  [0.2,1.0,1.0],  [0.4,1.0,1.0],  [0.6,1.0,1.0],  [0.8,1.0,1.0],
		   [0.0,0.09,0.2], [0.0,0.2,0.4],  [0.0,0.29,0.61],[0.0,0.4,0.8],  [0.0,0.5,1.0],  [0.2,0.6,1.0],  [0.4,0.69,1.0], [0.6,0.8,1.0],  [0.8,0.89,1.0],
		   [0.0,0.0,0.2],  [0.0,0.0,0.4],  [0.0,0.0,0.6],  [0.0,0.0,0.8],  [0.0,0.0,1.0],  [0.2,0.2,1.0],  [0.4,0.4,1.0],  [0.6,0.6,1.0],  [0.8,0.8,1.0],
		   

		   [0.69,0.36,0.36],  [0.70,0.36,0.31], [0.69,0.34,0.30], [0.70,0.32,0.29], [0.71,0.30,0.28], [0.69,0.30,0.28], [0.70,0.29,0.27], [0.71,0.28,0.26], [0.69,0.27,0.25], [0.70,0.26,0.24],
		   [0.64,0.35,0.35],  [0.64,0.34,0.34], [0.64,0.32,0.32], [0.64,0.30,0.30], [0.64,0.29,0.29], [0.64,0.28,0.28], [0.64,0.27,0.27], [0.64,0.26,0.26], [0.64,0.25,0.25], [0.64,0.24,0.24],
		   [0.65,0.29,0.15],  [0.65,0.28,0.14], [0.65,0.27,0.13], [0.65,0.26,0.12], [0.65,0.25,0.11], [0.65,0.24,0.10], [0.65,0.23,0.09], [0.65,0.23,0.08], [0.65,0.22,0.07], [0.65,0.21,0.06],  
		   [0.54,0.15,0.15],  [0.54,0.14,0.14], [0.54,0.13,0.13], [0.54,0.12,0.12], [0.54,0.11,0.11], [0.54,0.10,0.10], [0.54,0.09,0.09], [0.54,0.08,0.08], [0.54,0.07,0.07], [0.54,0.06,0.06], 
		   [0.6,0.18,0.28],   [0.6,0.17,0.27],  [0.6,0.16,0.26],  [0.6,0.15,0.25],  [0.6,0.14,0.24],  [0.6,0.13,0.23],  [0.6,0.12,0.22],  [0.6,0.11,0.21],  [0.6,0.10,0.20],  [0.6,0.09,0.19],  
		   [0.5,0.12,0.29],   [0.5,0.11,0.28],  [0.5,0.10,0.27],  [0.5,0.09,0.26],  [0.5,0.08,0.25],  [0.5,0.07,0.24],  [0.5,0.06,0.23],  [0.5,0.05,0.22],  [0.5,0.04,0.21],  [0.5,0.04,0.20],   
		   [1.0,0.29,0.47],   [1.0,0.28,0.46],  [1.0,0.27,0.45],  [1.0,0.26,0.44],  [1.0,0.25,0.43],  [1.0,0.24,0.42],  [1.0,0.23,0.41],  [1.0,0.22,0.40],  [1.0,0.21,0.39],  [1.0,0.20,0.48],   
		   [0.88,0.18,0.37],  [0.88,0.17,0.36], [0.88,0.16,0.35], [0.88,0.15,0.34], [0.88,0.14,0.33], [0.88,0.13,0.32], [0.88,0.12,0.31], [0.88,0.11,0.30], [0.88,0.10,0.29], [0.88,0.09,0.28], 
		    

		   [0.41,0.42,0.25],  [0.41,0.42,0.24], [0.41,0.42,0.23], [0.41,0.42,0.22], [0.41,0.42,0.21], [0.41,0.42,0.20], [0.41,0.42,0.19], [0.41,0.42,0.18], [0.41,0.42,0.17], [0.41,0.42,0.15], 
		   [0.72,0.75,0.41],  [0.72,0.75,0.40], [0.72,0.75,0.39], [0.72,0.75,0.38], [0.72,0.75,0.37], [0.72,0.75,0.36], [0.72,0.75,0.30], [0.72,0.75,0.25], [0.72,0.75,0.10], [0.72,0.75,0.05], 
		   [0.31,0.32,0.18],  [0.31,0.32,0.17], [0.31,0.32,0.15], [0.31,0.32,0.14], [0.31,0.32,0.12], [0.31,0.32,0.11], [0.31,0.32,0.10], [0.31,0.32,0.08], [0.31,0.32,0.05], [0.31,0.32,0.02],  
		   [0.21,0.48,0.36],  [0.20,0.48,0.36], [0.18,0.48,0.35], [0.17,0.48,0.35], [0.16,0.48,0.34], [0.15,0.48,0.34], [0.14,0.48,0.33], [0.13,0.48,0.33], [0.12,0.48,0.30], [0.10,0.48,0.25],  
		   [0.6,1.0,0.48],    [0.6,1.0,0.45],   [0.59,1.0,0.40],  [0.59,1.0,0.38],  [0.58,1.0,0.36],  [0.50,1.0,0.34],  [0.50,1.0,0.32],  [0.30,1.0,0.24],  [0.30,1.0,0.20],  [0.24,1.0,0.10],    
		   [0.73,1.0,0.0],    [0.70,1.0,0.0],   [0.64,1.0,0.0],   [0.6,1.0,0.0],    [0.58,1.0,0.0],   [0.55,1.0,0.0],   [0.41,1.0,0.0],   [0.39,1.0,0.0],   [0.35,1.0,0.0],   [0.19,0.9,0.0],
		   


		   [0.68,1.0,0.96],  [0.67,1.0,0.95],   [0.62,1.0,0.95],  [0.51,1.0,0.93],  [0.46,1.0,0.94],  [0.38,1.0,0.93],  [0.26,1.0,0.92],  [0.17,1.0,0.91],  [0.07,1.0,0.90],  [0.0,1.0,0.89],   
		   [0.28,0.42,0.41], [0.26,0.4,0.38],   [0.26,0.42,0.40], [0.21,0.38,0.36], [0.18,0.4,0.37],  [0.19,0.49,0.46], [0.12,0.52,0.48], [0.08,0.55,0.5],  [0.03,0.53,0.47], [0.0,0.6,0.52],
		   [0.71,1.0,0.95],  [0.69,1.0,0.94],   [0.66,1.0,0.94],  [0.62,1.0,0.94],  [0.54,1.0,0.92],  [0.46,1.0,0.9],   [0.38,1.0,0.9],   [0.28,1.0,0.89],  [0.18,1.0,0.87],  [0.05,1.0,0.85],
		   [0.7,1.0,0.99],   [0.65,1.0,0.99],   [0.6,1.0,0.99],   [0.55,1.0,0.99],  [0.5,1.0,0.99],   [0.45,1.0,0.99],  [0.3,1.0,0.99],   [0.2,1.0,0.99],   [0.1,1.0,0.99],   [0.05,1.0,0.99], 
		   [0.32,0.32,0.55], [0.30,0.30,0.55],  [0.26,0.26,0.55], [0.24,0.24,0.55], [0.18,0.18,0.55], [0.16,0.16,0.55], [0.12,0.12,0.55], [0.10,0.10,0.55], [0.09,0.09,0.55], [0.05,0.05,0.55], 
		   [0.32,0.2,0.56],  [0.3,0.18,0.55],   [0.25,0.12,0.51], [0.23,0.1,0.5],   [0.2,0.06,0.47],  [0.16,0.03,0.44], [0.14,0.01,0.4],  [0.16,0.05,0.37], [0.32,0.21,0.54], [0.43,0.26,0.77],
		   [0.45,0.5,1.0],   [0.43,0.48,1.0],   [0.41,0.46,1.0],  [0.34,0.4,1.0],   [0.3,0.36,1.0],   [0.22,0.29,1.0],  [0.15,0.22,1.0],  [0.1,0.18,1.0],   [0.07,0.1,0.46],  [0.23,0.26,0.53],
		   ]


targets = [[0],  [0],  [0],  [0],  [0],  [0],  [0],  [0],  [0],
		   [0],  [0],  [0],  [0],  [0],  [0],  [0],  [0],  [0],
		   [0.5],[0.5],[0.5],[0.5],
		   [0.5],[0.5],[0.5],[0.5],[0.5],[0.5],[0.5],[0.5],[0.5],
		   [0.5],[0.5],[0.5],[0.5],[0.5],[0.5],[0.5],[0.5],[0.5],
		   [0.5],[0.5],[0.5],[0.5],[0.5],[0.5],[0.5],[0.5],[0.5],
		   [1.0],[1.0],[1.0],[1.0],[1.0],[1.0],[1.0],[1.0],[1.0],
		   [1.0],[1.0],[1.0],[1.0],[1.0],[1.0],[1.0],[1.0],[1.0],
		   [1.0],[1.0],[1.0],[1.0],[1.0],[1.0],[1.0],[1.0],[1.0],
		   

		   [0],  [0],  [0],  [0],  [0],  [0],  [0],  [0],  [0], [0],
		   [0],  [0],  [0],  [0],  [0],  [0],  [0],  [0],  [0], [0],
		   [0],  [0],  [0],  [0],  [0],  [0],  [0],  [0],  [0], [0],
		   [0],  [0],  [0],  [0],  [0],  [0],  [0],  [0],  [0], [0],
		   [0],  [0],  [0],  [0],  [0],  [0],  [0],  [0],  [0], [0],
		   [0],  [0],  [0],  [0],  [0],  [0],  [0],  [0],  [0], [0],
		   [0],  [0],  [0],  [0],  [0],  [0],  [0],  [0],  [0], [0],
		   [0],  [0],  [0],  [0],  [0],  [0],  [0],  [0],  [0], [0],



		   [0.5],[0.5],[0.5],[0.5],[0.5],[0.5],[0.5],[0.5],[0.5],[0.5],
		   [0.5],[0.5],[0.5],[0.5],[0.5],[0.5],[0.5],[0.5],[0.5],[0.5],
		   [0.5],[0.5],[0.5],[0.5],[0.5],[0.5],[0.5],[0.5],[0.5],[0.5],
		   [0.5],[0.5],[0.5],[0.5],[0.5],[0.5],[0.5],[0.5],[0.5],[0.5],
		   [0.5],[0.5],[0.5],[0.5],[0.5],[0.5],[0.5],[0.5],[0.5],[0.5],
		   [0.5],[0.5],[0.5],[0.5],[0.5],[0.5],[0.5],[0.5],[0.5],[0.5],



		   [1.0],[1.0],[1.0],[1.0],[1.0],[1.0],[1.0],[1.0],[1.0],[1.0],
		   [1.0],[1.0],[1.0],[1.0],[1.0],[1.0],[1.0],[1.0],[1.0],[1.0],
		   [1.0],[1.0],[1.0],[1.0],[1.0],[1.0],[1.0],[1.0],[1.0],[1.0],
		   [1.0],[1.0],[1.0],[1.0],[1.0],[1.0],[1.0],[1.0],[1.0],[1.0],
		   [1.0],[1.0],[1.0],[1.0],[1.0],[1.0],[1.0],[1.0],[1.0],[1.0],
		   [1.0],[1.0],[1.0],[1.0],[1.0],[1.0],[1.0],[1.0],[1.0],[1.0],
		   [1.0],[1.0],[1.0],[1.0],[1.0],[1.0],[1.0],[1.0],[1.0],[1.0],
		   ]

reps=1000

#user input
userR = (float (input ("Enter Red Value: ")))/255
userG = (float (input ("Enter Green Value: ")))/255
userB = (float (input ("Enter Blue Value: ")))/255

#makes an empty list to contain the neural net
network =[]

#sets up the network to accommodate the size of your inputs
network = neuro.setup_network(inputs)

#trains the network for some number of repetitions on
neuro.train(network, inputs, targets, reps)



test_input = [userR, userG, userB]

#predicts the outcome based on the input
pred = neuro.predict(network,test_input)

pred = (float(pred))

if pred < 0.33:
	print "Red"

elif pred >= 0.33 and pred < 0.66:
	print "Green"

else :
	print "Blue"

