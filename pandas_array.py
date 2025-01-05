# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 15:13:59 2024

@author: ageffre
"""

import pandas as pd

solved = False
column1 = 0
column2 = 0
column3 = 0
column4 = 0
column5 = 0
activecolumn1 = 0
activecolumn2 = 0
activecolumn3 = 0
activecolumn4 = 0
activecolumn5 = 0
cell1 = 0
cell2 = 0
cell3 = 0
cell4 = 0

pass1 = [0,0,0,0]
pass2 = [0,0,0,0]
pass3 = [0,0,0,0]
pass4 = [0,0,0,0]
pass5 = [0,0,0,0]
pass6 = [0,0,0,0]
pass7 = [0,0,0,0]
pass8 = [0,0,0,0]
pass9 = [0,0,0,0]
pass10 = [0,0,0,0]
pass11 = [0,0,0,0]
pass12 = [0,0,0,0]

passcount = 0


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
print("Layer 5:")
print(layer5)
print("")
layer4 = pd.read_csv(r'C:\Users\alexg\Documents\Python Scripts\Mayan_Puzzle\Mayan_Puzzle\Calendar_Puzzle\Mayan Puzzle - Data with placeholder zeroes.csv', names=['A','B','C','D','E','F','G','H','I','J','K','L'], skiprows = lambda x: x not in layer4rows)
print("Layer 4:")
print(layer4)
print("")
layer3 = pd.read_csv(r'C:\Users\alexg\Documents\Python Scripts\Mayan_Puzzle\Mayan_Puzzle\Calendar_Puzzle\Mayan Puzzle - Data with placeholder zeroes.csv', names=['A','B','C','D','E','F','G','H','I','J','K','L'], skiprows = lambda x: x not in layer3rows)
print("Layer 3:")
print(layer3)
print("")
layer2 = pd.read_csv(r'C:\Users\alexg\Documents\Python Scripts\Mayan_Puzzle\Mayan_Puzzle\Calendar_Puzzle\Mayan Puzzle - Data with placeholder zeroes.csv', names=['A','B','C','D','E','F','G','H','I','J','K','L'], skiprows = lambda x: x not in layer2rows)
print("Layer 2:")
print(layer2)
print("")
layer1 = pd.read_csv(r'C:\Users\alexg\Documents\Python Scripts\Mayan_Puzzle\Mayan_Puzzle\Calendar_Puzzle\Mayan Puzzle - Data with placeholder zeroes.csv', names=['A','B','C','D','E','F','G','H','I','J','K','L'], skiprows = lambda x: x not in layer1rows)
print("Layer 1:")
print(layer1)
print("")


################################################################################################
# This section takes the active column in each row and stacks the values on top of each other. #
# The highest numbered layer with a value is passed to that cell.                              #
################################################################################################

def stack():
    
    global activecolumn5
    global activecolumn4
    global activecolumn3
    global activecolumn2
    global activecolumn1
    
    global cell1 # This is the innermost ring of the puzzle. Values from all layers can exist here.
    if (layer5.iat[3,activecolumn5] > 0):
        cell1 = layer5.iat[3,activecolumn5]
    elif (layer4.iat[3,activecolumn4] > 0):
        cell1 = layer4.iat[3,activecolumn4]
    elif (layer3.iat[3,activecolumn3] > 0):
        cell1 = layer3.iat[3,activecolumn3]
    elif (layer2.iat[3,activecolumn2] > 0):
        cell1 = layer2.iat[3,activecolumn2]
    else: 
        cell1 = layer1.iat[3,activecolumn1]

    global cell2 # This is second ring of the puzzle from the center. Values from all layers except 5 can exist here. 
    if (layer5.iat[2,activecolumn5] > 0):
        cell2 = layer5.iat[2,activecolumn5]
    elif (layer4.iat[2,activecolumn4] > 0):
        cell2 = layer4.iat[2,activecolumn4]
    elif (layer3.iat[2,activecolumn3] > 0):
        cell2 = layer3.iat[2,activecolumn3]
    elif (layer2.iat[2,activecolumn2] > 0):
        cell2 = layer2.iat[2,activecolumn2]
    else: 
        cell2 = layer1.iat[2,activecolumn1]

    global cell3 # This is the 3rd ring of the puzzle from the center. Values from Layers 1-3 can exist here.
    if (layer5.iat[1,activecolumn5] > 0):
        cell3 = layer5.iat[1,activecolumn5]
    elif (layer4.iat[1,activecolumn4] > 0):
        cell3 = layer4.iat[1,activecolumn4]
    elif (layer3.iat[1,activecolumn3] > 0):
        cell3 = layer3.iat[1,activecolumn3]
    elif (layer2.iat[1,activecolumn2] > 0):
        cell3 = layer2.iat[1,activecolumn2]
    else: 
        cell3 = layer1.iat[1,activecolumn1]
 
    
    global cell4 # This is the outermost ring of the puzzle. Only values from layers 1 and 2 can exist here.  
    if (layer5.iat[0,activecolumn5] > 0):
        cell4 = layer5.iat[0,activecolumn5]
    elif (layer4.iat[0,activecolumn4] > 0):
        cell4 = layer4.iat[0,activecolumn4]
    elif (layer3.iat[0,activecolumn3] > 0):
        cell4 = layer3.iat[0,activecolumn3]
    elif (layer2.iat[0,activecolumn2] > 0):
        cell4 = layer2.iat[0,activecolumn2]
    else: 
        cell4 = layer1.iat[0,activecolumn1]
        
########################################################################################
# This section is a rolling index that works similar to an analog odometer.            #
# When layer 5 index rolls over to 0, layer 4 is indexed by one.                       # 
# The process repeats with layers 3, 2, and 1 as the layer above is indexed back to 0. #
########################################################################################

def index5(): # Start by rotating the topmost layer of the puzzle one at a time.
    
    global column5
    
    if (column5 < 11):
        column5 = (column5 + 1)
    else:
        column5 = 0
        index4()
    
def index4(): # Rotate the second layer from the top one position as layer 5 indexes back to 0.
    
    global column4
    
    if (column4 < 11):
        column4 = (column4 + 1)
    else:
        column4 = 0
        index3()
    
def index3(): # Rotate the third layer from the top one position as layer 4 indexes back to 0.
    
    global column3
    
    if (column3 < 11):
        column3 = (column3 + 1)
    else:
        column3 = 0
        index2()
    
def index2(): # Rotate the fourth layer from the top one position as layer 3 indexes back to 0.
    
    global column2
    
    if (column2 < 11):
        column2 = (column2 + 1)
    else:
        column2 = 0
        index1()

def index1(): # Rotate the bottom layer one position as layer 2 indexes back to 0.

    global column1    
    
    if (column1 < 11):
        column1 = (column1 + 1)
    else:
        column1 = 0
        print("Analysis failed")
        
def nextcolumn():
    
    global activecolumn1
    global activecolumn2
    global activecolumn3
    global activecolumn4
    global activecolumn5
    
    if (activecolumn1 < 11):
        activecolumn1 = (activecolumn1 + 1)
    else:
        activecolumn1 = 0
        
    if (activecolumn2 < 11):
        activecolumn2 = (activecolumn2 + 1)
    else:
        activecolumn2 = 0

    if (activecolumn3 < 11):
        activecolumn3 = (activecolumn3 + 1)
    else:
        activecolumn3 = 0

    if (activecolumn4 < 11):
        activecolumn4 = (activecolumn4 + 1)
    else:
        activecolumn4 = 0

    if (activecolumn5 < 11):
        activecolumn5 = (activecolumn5 + 1)
    else:
        activecolumn5 = 0

    
# stack()
# print(cell1)
# print(cell2)
# print(cell3)
# print(cell4)

    
    
def checkresult():
    
    global passcount
    global cell1
    global cell2
    global cell3
    global cell4
    global solved
    global activecolumn1
    global activecolumn2
    global activecolumn3
    global activecolumn4
    global activecolumn5
    global column1
    global column2
    global column3
    global column4
    global column5
    global pass1
    global pass2
    global pass3
    global pass4
    global pass5
    global pass6
    global pass7
    global pass8
    global pass9
    global pass10
    global pass11
    global pass12
    
    
    if (cell1 + cell2 + cell3 + cell4) == 42:
        passcount = (passcount + 1)
        print("Passed ", passcount, " out of 12.")
        if (passcount == 1):
            pass1 = [cell1,cell2,cell3,cell4]
            nextcolumn()
        elif (passcount == 2):
            pass2 = [cell1,cell2,cell3,cell4]
            nextcolumn()
        elif (passcount == 3):
            pass3 = [cell1,cell2,cell3,cell4]
            nextcolumn()
        elif (passcount == 4):
            pass4 = [cell1,cell2,cell3,cell4]
            nextcolumn()
        elif (passcount == 5):
            pass5 = [cell1,cell2,cell3,cell4]
            nextcolumn()
        elif (passcount == 6):
            pass6 = [cell1,cell2,cell3,cell4]
            nextcolumn()
        elif (passcount == 7):
            pass7 = [cell1,cell2,cell3,cell4]
            nextcolumn()
        elif (passcount == 8):
            pass8 = [cell1,cell2,cell3,cell4]
            nextcolumn()
        elif (passcount == 9):
            pass9 = [cell1,cell2,cell3,cell4]
            nextcolumn()
        elif (passcount == 10):
            pass10 = [cell1,cell2,cell3,cell4]
            nextcolumn()
        elif (passcount == 11):
            pass11 = [cell1,cell2,cell3,cell4]
            nextcolumn()
        elif (passcount == 12):
            pass12 = [cell1,cell2,cell3,cell4]
            solved = True
            print("Puzzle Solved!")
            print("Column A")
            print(pass1)
            print("Column B")
            print(pass2)
            print("Column C")
            print(pass3)
            print("Column D")
            print(pass4)
            print("Column E")
            print(pass5)
            print("Column F")
            print(pass6)
            print("Column G")
            print(pass7)
            print("Column H")
            print(pass8)
            print("Column I")
            print(pass9)
            print("Column J")
            print(pass10)
            print("Column K")
            print(pass11)
            print("Column L")
            print(pass12)
            print("Bottom Layer")
            print(column1)
            print("Second Layer")
            print(column2)
            print("Third Layer")
            print(column3)
            print("Fourth Layer")
            print(column4)
            print("Fifth Layer")
            print(column5)
            
            
    else:
        print("No match. Indexing...")
        passcount = 0
        index5()
        activecolumn5 = column5
        activecolumn4 = column4
        activecolumn3 = column3
        activecolumn2 = column2
        activecolumn1 = column1
        
        
while solved == False:

    stack()
    print("Stacking")
    checkresult()
    