# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 15:13:59 2024

@author: ageffre
"""

import pandas as pd

solved = False
row = 0
column = 0
cell1 = 0
cell2 = 0
cell3 = 0
cell4 = 0

# puzzle = pd.read_csv('C:/Users/alexg/Documents/Python Scripts/Mayan_Puzzle/Mayan_Puzzle/Calendar_Puzzle/Mayan Puzzle - Data with no placeholders.csv', names=['A','B','C','D','E','F','G','H','I','J','K','L'])
# puzzle = pd.read_csv('C:/Users/alexg/Documents/Python Scripts/Mayan_Puzzle/Mayan_Puzzle/Calendar_Puzzle/Mayan Puzzle - Data with no placeholders.csv', names=['A','B','C','D','E','F','G','H','I','J','K','L'])

# print(puzzle)


# layer5 = puzzle.iloc[16:20]
# layer4 = puzzle.iloc[12:16]
# layer3 = puzzle.iloc[8:12]
# layer2 = puzzle.iloc[4:8]
# layer1 = puzzle.iloc[0:4]
layer5rows = [16,17,18,19,20]
layer4rows = [12,13,14,15]
layer3rows = [8,9,10,11]
layer2rows = [4,5,6,7]
layer1rows = [0,1,2,3]


layer5 = pd.read_csv(r'C:\Users\alexg\Documents\Python Scripts\Mayan_Puzzle\Mayan_Puzzle\Calendar_Puzzle\Mayan Puzzle - Data with placeholder zeroes.csv', names=['A','B','C','D','E','F','G','H','I','J','K','L'], skiprows = lambda x: x not in layer5rows)
layer4 = pd.read_csv(r'C:\Users\alexg\Documents\Python Scripts\Mayan_Puzzle\Mayan_Puzzle\Calendar_Puzzle\Mayan Puzzle - Data with placeholder zeroes.csv', names=['A','B','C','D','E','F','G','H','I','J','K','L'], skiprows = lambda x: x not in layer4rows)
layer3 = pd.read_csv(r'C:\Users\alexg\Documents\Python Scripts\Mayan_Puzzle\Mayan_Puzzle\Calendar_Puzzle\Mayan Puzzle - Data with placeholder zeroes.csv', names=['A','B','C','D','E','F','G','H','I','J','K','L'], skiprows = lambda x: x not in layer3rows)
layer2 = pd.read_csv(r'C:\Users\alexg\Documents\Python Scripts\Mayan_Puzzle\Mayan_Puzzle\Calendar_Puzzle\Mayan Puzzle - Data with placeholder zeroes.csv', names=['A','B','C','D','E','F','G','H','I','J','K','L'], skiprows = lambda x: x not in layer2rows)
layer1 = pd.read_csv(r'C:\Users\alexg\Documents\Python Scripts\Mayan_Puzzle\Mayan_Puzzle\Calendar_Puzzle\Mayan Puzzle - Data with placeholder zeroes.csv', names=['A','B','C','D','E','F','G','H','I','J','K','L'], skiprows = lambda x: x not in layer1rows)

# layer2 = 
# layer1 = 

print('')
print('')
print(layer5)
print('')
print(layer4)
print('')
print(layer3)
print(layer2)
print('')
print(layer1)
print('')


def stack():
    global cell1
    global cell2
    global cell3
    global cell4
# Layer row 3 of the defined column and set cell1 to the value that would show in that orientation
    if (layer5.iat[3,column] > 0):
        cell1 = layer5.iat[row,column]
    elif (layer4.iat[3,column] > 0):
        cell1 = layer4.iat[row,column]
    elif (layer3.iat[3,column] > 0):
        cell1 = layer3.iat[row,column]
    elif (layer2.iat[3,column] > 0):
        cell1 = layer2.iat[row,column]
    else: 
        cell1 = layer1.iat[3,column]
        
    if (layer5.iat[2,column] > 0):
        cell2 = layer5.iat[row,column]
    elif (layer4.iat[2,column] > 0):
        cell2 = layer4.iat[row,column]
    elif (layer3.iat[2,column] > 0):
        cell2 = layer3.iat[row,column]
    elif (layer2.iat[2,column] > 0):
        cell2 = layer2.iat[row,column]
    else: 
        cell2 = layer1.iat[2,column]
        
    if (layer5.iat[1,column] > 0):
        cell3 = layer5.iat[row,column]
    elif (layer4.iat[1,column] > 0):
        cell3 = layer4.iat[row,column]
    elif (layer3.iat[1,column] > 0):
        cell3 = layer3.iat[row,column]
    elif (layer2.iat[1,column] > 0):
        cell3 = layer2.iat[row,column]
    else: 
        cell3 = layer1.iat[1,column]
        
    if (layer5.iat[0,column] > 0):
        cell4 = layer5.iat[row,column]
    elif (layer4.iat[0,column] > 0):
        cell4 = layer4.iat[row,column]
    elif (layer3.iat[0,column] > 0):
        cell4 = layer3.iat[row,column]
    elif (layer2.iat[0,column] > 0):
        cell4 = layer2.iat[row,column]
    else: 
        cell4 = layer1.iat[0,column]
        

        
    
stack()
print(cell1)
print(cell2)
print(cell3)
print(cell4)
# while solved != False:
    