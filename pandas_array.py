# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 15:13:59 2024

@author: ageffre
"""

import pandas as pd

solved = False
row = 0
column = 0

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

layer5 = pd.read_csv('C:/Users/alexg/Documents/Python Scripts/Mayan_Puzzle/Mayan_Puzzle/Calendar_Puzzle/Mayan Puzzle - Data with no placeholders.csv', names=['A','B','C','D','E','F','G','H','I','J','K','L'], skiprows = lambda x: x not in layer5rows)
layer4 = pd.read_csv('C:/Users/alexg/Documents/Python Scripts/Mayan_Puzzle/Mayan_Puzzle/Calendar_Puzzle/Mayan Puzzle - Data with no placeholders.csv', names=['A','B','C','D','E','F','G','H','I','J','K','L'], skiprows = lambda x: x not in layer4rows)
layer3 = pd.read_csv('C:/Users/alexg/Documents/Python Scripts/Mayan_Puzzle/Mayan_Puzzle/Calendar_Puzzle/Mayan Puzzle - Data with no placeholders.csv', names=['A','B','C','D','E','F','G','H','I','J','K','L'], skiprows = lambda x: x not in layer3rows)
layer2 = pd.read_csv('C:/Users/alexg/Documents/Python Scripts/Mayan_Puzzle/Mayan_Puzzle/Calendar_Puzzle/Mayan Puzzle - Data with no placeholders.csv', names=['A','B','C','D','E','F','G','H','I','J','K','L'], skiprows = lambda x: x not in layer2rows)
layer1 = pd.read_csv('C:/Users/alexg/Documents/Python Scripts/Mayan_Puzzle/Mayan_Puzzle/Calendar_Puzzle/Mayan Puzzle - Data with no placeholders.csv', names=['A','B','C','D','E','F','G','H','I','J','K','L'], skiprows = lambda x: x not in layer1rows)

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

print(layer1.iat[0,1])

def stack():
    cell1 = layer1.iat[row,column]
    cell1 = (
        if layer2.iat[row,column] != NaN
            layer2.iat[row,column]
        else layer1.iat[row,column])
    

while solved != False:
    