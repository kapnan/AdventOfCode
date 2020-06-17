import os
import numpy as np
import sys


with open("C:/Users/kriti/Documents/Learning Python/AdventOfCode/2019/Data/Cab1.txt") as f:
    Data1 = np.genfromtxt(f,dtype=str, delimiter = ',', )
with open("C:/Users/kriti/Documents/Learning Python/AdventOfCode/2019/Data/Cab2.txt") as g:
    Data2 = np.genfromtxt(g, dtype = str, delimiter = ',')
print ('imported data', Data1)

Start = []

Start = [0,0]

CurrentPosition = []
CurrentPosition = Start.copy()
print('cp=', CurrentPosition)

PositionArr = [[ 0 for i in range(999)] for i in range(999)]
Length1 = len(Data1)
Length2 = len(Data2)

for x in range(len(Data1)):
    instruction = Data1[x]
    direct = instruction[0]
    dist = int(instruction[1:])
    ##print(instruction[0])
    ##print (dist)
    if direct == 'U':
        for d in range(dist):
            PositionArr.append[ CurrentPosition[1] , CurrentPosition[2] + d ] = 1
##    
##               
##    
####    table = { 'U' : '+i', 'D' : '-i', 'L' : '-', 'R' : '+' }
