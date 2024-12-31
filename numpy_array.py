# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 15:19:15 2024

@author: ageffre
"""
 
# To import the Numpy package
import numpy as np
import pandas as pd

##################################################################
##  This is the physical makeup of the puzzle.                  ##
##  Each layer is represented as a numpy array.                 ##
##  A zero in the array symbolizes a cutout to the layer below  ##
##################################################################

# This is the base layer of the puzzle
np_layer_1 = np.array([[3,4,12,2,5,10,7,16,8,7,8,8], 
                    [4,6,6,3,3,14,14,21,21,9,9,4],
                    [5	,6,7,8,9,10,11,12,13,14,15,4],
                    [11,14,11,14,11,14,14,11,14,11,14,11]])

# This is the second layer of the puzzle
np_layer_2 = np.array([[12,0,6,0,10,0,10,0,1,0,9,0],
                    [2	,13,9,0,17,19,3,12,3,26,6,0],
                    [6	,0,14,12,13,8,9,0,9,20,12,3],
                    [7	,14,11,0,8,0,16,2,7,0,9,0]])

# This is the third layer of the puzzle
np_layer_3 = np.array([[0,0,0,0,0,0,0,0,0,0,0,0],
                    [16,0,9,0,5,0,10,0,8,0,22,0],
                    [14,1,12,0,21,6,15,4,9,18,11,26],
                    [5,0,7,8,9,13,9,7,13,21,17,4]])

# This is the fourth layer of the puzzle
np_layer_4 = np.array([[0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0],
                    [15,0,0,14,0,9,0,12,0,4,0,7],
                    [6,0,11,11,6,11,0,6,17,7,3,0]])

# This is the fifth layer of the puzzle
np_layer_5 = np.array([[0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0],
                    [10,0,7,0,15,0,8,0,3,0,6,0]])

print("These are numpy arrays")
print("Layer 1:")
print(np_layer_1)
print("Layer 2:")
print(np_layer_2)
print("Layer 3:")
print(np_layer_3)
print("Layer 4:")
print(np_layer_4)
print("Layer 5:")
print(np_layer_5)