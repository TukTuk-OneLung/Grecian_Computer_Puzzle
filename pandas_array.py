# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 15:13:59 2024

@author: ageffre
"""

import pandas as pd

puzzle = pd.read_csv('C:/Users/ageffre/Documents/Python/Mayan Puzzle/Mayan Puzzle - Data with no placeholders.csv', names=['A','B','C','D','E','F','G','H','I','J','K','L'])

print(puzzle)

layer5 = puzzle.iloc[16:20]
layer4 = puzzle.iloc[12:16]
layer3 = puzzle.iloc[8:12]
layer2 = puzzle.iloc[4:8]
layer1 = puzzle.iloc[0:4]


print(layer5)
print('')
print(layer4)
print('')
print(layer3)
print('')
print(layer2)
print('')
print(layer1)
print('')
