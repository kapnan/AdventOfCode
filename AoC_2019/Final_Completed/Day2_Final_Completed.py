import numpy as np
import os
import sys


os.chdir("C:/Users/kriti/Documents/Learning Python/AdventOfCode/2019")
with open("Intcode.txt",'r') as f:
    ints = np.genfromtxt(f,dtype=int, delimiter=',') #or ints = list(map(int,f)). This assigns the list to variable ints
    CP = ints.copy()
##nouns = range(0,99)
##verbs = range(0,99)
for v in range(0,99):
    for n in range(0,99):

       
        ints = CP.copy()
        ints[1] = n
        ints[2] = v

        #print(ints)
        copy = [] #initialises a checker to check when no more changes are occuring
        i = 0 #Initialise the indexing for stepping through ints
        i_3 = i+3


        while i_3 < len(ints):
            
            i1 = int(ints[i+1]) #resets i values for new loop of value for i. This process reads the values in the 4 block chain and assigns them (the locations) to variables
            i2 = int(ints[i+2])
            i3 = int(ints[i+3])
            
            
            if ints[i] == 1:
                ints[i3]= ints[i1] + ints[i2]
                

            elif ints[i] == 2:
                ints[i3] = ints[i1]*ints[i2]
            
            elif ints[i] == 3:              #added for Day_5
                ints[i1] = int(input('value:'))
            
            elif ints[i] == 4:              #Added for Day_5
                print('Opcode 4 value is: ', ints[i1])
                    

            elif ints[i] == 99:
                
                #print('is this it?')
                #print(ints)
                
                if ints[0] == 19690720:
                    print("noun =", n, ", verb =", v)
                    #print(ints)
                    sys.exit('reached 19690720')
                

            i += 4
            i_3 = i+3
            
            
         
   
    

       

        
 



        





        
        
            













