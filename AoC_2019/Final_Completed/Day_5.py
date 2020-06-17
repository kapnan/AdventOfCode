# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 11:15:50 2020

@author: kriti
"""

#import math
import numpy as np
import os 
import sys
import time

if __name__ = '__main__':
    print('Hello, I am Day_5 :)')


def Day_5():
    
    t = time.time()
    
    os.chdir("C:/Users/kriti/Documents/Learning Python/AdventOfCode/2019")
    with open("Data/Intcode_Day5.txt",'r') as f:
        ints = np.genfromtxt(f,dtype=int, delimiter=',') #or ints = list(map(int,f)). This assigns the list to variable ints
        #CP = ints.copy()
    ##nouns = range(0,99)
    ##verbs = range(0,99)

    
           
    #ints = CP.copy()
   

    #print(ints)
    #copy = [] #initialises a checker to check when no more changes are occuring
    i = 0 #Initialise the indexing for stepping through ints
    i_3 = i+3


    while (i_3 < len(ints)and (i+1) < len(ints)):
        
# =============================================================================
#         if int(i)/(10**4) > 1 :
#             i3 = i+3
#         elif int(i)/(10**3):
#             
#             
#         elif int(i)/10 < 1:
#             i1 = int(ints[i+1]) #resets i values for new loop of value for i. This process reads the values in the 4 block chain and assigns them (the locations) to variables
#             i2 = int(ints[i+2])
#             i3 = int(ints[i+3])
# =============================================================================

        opcode = str(ints[i])      
        
        i1 = int(ints[i+1]) #resets i values for new loop of value for i. This process reads the values in the 4 block chain and assigns them (the locations) to variables
        i2 = int(ints[i+2])
        i3 = int(ints[i+3])
       # print('o')
        try:

            opcode_num = opcode[-1] 
            if opcode_num =='9':
                opcode_num ='99'
           
            if opcode[-3] == '1':
                i1 = i+1
            # elif opcode[-3] == '0':
            #     i1 = int(ints[i+1])
            if opcode[-4] == '1':
                i2 = i+2
            # elif opcode[-4] == '0':
            #     i2 = int(ints[i+2])
            if opcode[-5] == '1':
                i3 = i+3
            # elif opcode[-5] =='0':
            #     i3 = int(ints[i+3])
           # print('x')             
        except IndexError:
            #print('x') 
            pass
       # print('opcode num is', opcode_num)

        #opcode = str(ints[i])
        
        
        # if (len(opcode) == 1 ):
        #     opcode_num = int(opcode[-1])
        # else:
        #     opcode_num = int(opcode[-2]+opcode[-1]) #Needed as 99 is a possibility for the opcode 
        # print(opcode_num)
        
        
        
        if opcode_num == '1':
            ints[i3]= ints[i1] + ints[i2]
            
            i+= 4
        elif opcode_num == '2':
            ints[i3] = ints[i1]*ints[i2]
            i+=4
        elif opcode_num == '3':              #added for Day_5
            ints[i1] = int(input('value:'))
            #ints[i1] = 3
            i+=2
        elif opcode_num == '4':              #Added for Day_5
            i+=2
            print('Opcode 4 value is: ', ints[i1])
            print((time.time()-t)*1000, 'ms to complete')
            
            sys.exit('Done')
        elif opcode_num == '5':
            if (ints[i1] != 0):
                i = ints[i2]

            else:
                i+=3
        elif opcode_num == '6':
            if ints[i1] == 0:
                i = ints[i2]
            else:
                i+=3
        elif opcode_num == '7':
            if ints[i1] < ints[i2]:
                ints[i3] = 1
                
            else:
                ints[i3] = 0
            i+=4
        elif opcode_num =='8':
            if ints[i1] == ints[i2]:
                ints[i3] = 1
                
            else:
                ints[i3] = 0
            i+=4
            

        #elif ints[i] == 99:
        #sys.exit(opcode_num == '99')
            #print('is this it?')
            #print(ints)
        if opcode_num == '99':
            print('HALTED')
            print(time.time()-t)
            sys.exit()
    
# =============================================================================
#             if ints[0] == 19690720:
#                 print("noun =", n, ", verb =", v)
#                 #print(ints)
#                 sys.exit('reached 19690720')
# =============================================================================
            

        #i += 4
        #i_3 = i+3
