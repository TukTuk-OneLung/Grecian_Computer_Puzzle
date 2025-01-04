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




def stack():
    
    global column5
    global column4
    global column3
    global column2
    global column1
    
    # Layer row 3 of the defined column and set cell1 to the value that would show in that orientation
    global cell1
    if (layer5.iat[3,column5] > 0):
        cell1 = layer5.iat[3,column5]
    elif (layer4.iat[3,column4] > 0):
        cell1 = layer4.iat[3,column4]
    elif (layer3.iat[3,column3] > 0):
        cell1 = layer3.iat[3,column3]
    elif (layer2.iat[3,column2] > 0):
        cell1 = layer2.iat[3,column2]
    else: 
        cell1 = layer1.iat[3,column1]

    global cell2        
    if (layer5.iat[2,column5] > 0):
        cell2 = layer5.iat[2,column5]
    elif (layer4.iat[2,column4] > 0):
        cell2 = layer4.iat[2,column4]
    elif (layer3.iat[2,column3] > 0):
        cell2 = layer3.iat[2,column3]
    elif (layer2.iat[2,column2] > 0):
        cell2 = layer2.iat[2,column2]
    else: 
        cell2 = layer1.iat[2,column1]

    global cell3
    if (layer5.iat[1,column5] > 0):
        cell3 = layer5.iat[1,column5]
    elif (layer4.iat[1,column4] > 0):
        cell3 = layer4.iat[1,column4]
    elif (layer3.iat[1,column3] > 0):
        cell3 = layer3.iat[1,column3]
    elif (layer2.iat[1,column2] > 0):
        cell3 = layer2.iat[1,column2]
    else: 
        cell3 = layer1.iat[1,column1]
 
    
    global cell4    
    if (layer5.iat[0,column5] > 0):
        cell4 = layer5.iat[0,column5]
    elif (layer4.iat[0,column4] > 0):
        cell4 = layer4.iat[0,column4]
    elif (layer3.iat[0,column3] > 0):
        cell4 = layer3.iat[0,column3]
    elif (layer2.iat[0,column2] > 0):
        cell4 = layer2.iat[0,column2]
    else: 
        cell4 = layer1.iat[0,column1]
        
        
def index5():
    
    global column5
    
    if (column5 <=11):
        column5 = (column5 + 1)
    else:
        column5 = 0
        index4()
    
def index4():
    
    global column4
    
    if (column4 <=11):
        column4 = (column5 + 1)
    else:
        column4 = 0
        index3()
    
def index3():
    
    global column3
    
    if (column3 <=11):
        column3 = (column5 + 1)
    else:
        column3 = 0
        index2()
    
def index2():
    
    global column2
    
    if (column2 <=11):
        column2 = (column5 + 1)
    else:
        column2 = 0
        index1()

def index1():

    global column1    
    
    if (column1 <=11):
        column1 = (column5 + 1)
    else:
        column1 = 0
        print("Analysis failed")
        

        
    
stack()
print(cell1)
print(cell2)
print(cell3)
print(cell4)


while solved != False:
    stack()
    
    if (sum(cell1,cell2,cell3,cell4) == 42):
        passcount = (passcount + 1)
        print("Passed ", passcount, " out of 12.")
        if (passcount == 1):
            pass1 = [cell1,cell2,cell3,cell4]
        elif (passcount == 2):
            pass2 = [cell1,cell2,cell3,cell4]
        elif (passcount == 3):
            pass3 = [cell1,cell2,cell3,cell4]
        elif (passcount == 4):
            pass4 = [cell1,cell2,cell3,cell4]
        elif (passcount == 5):
            pass5 = [cell1,cell2,cell3,cell4]
        elif (passcount == 6):
            pass6 = [cell1,cell2,cell3,cell4]
        elif (passcount == 7):
            pass7 = [cell1,cell2,cell3,cell4]
        elif (passcount == 8):
            pass8 = [cell1,cell2,cell3,cell4]
        elif (passcount == 9):
            pass9 = [cell1,cell2,cell3,cell4]
        elif (passcount == 10):
            pass10 = [cell1,cell2,cell3,cell4]
        elif (passcount == 11):
            pass11 = [cell1,cell2,cell3,cell4]
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
            
            
    else:
        index5()
        
        
        #function that shifts layer 5 to the next column
    