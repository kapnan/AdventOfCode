import numpy as np
import os
import sys


os.chdir("C:/Users/kriti/Documents/Learning Python/AdventOfCode/2019")
with open("Intcode.txt",'r') as f:
    ints = np.genfromtxt(f,dtype=int, delimiter=',') #or ints = list(map(int,f)). This assigns the list to variable ints

print(ints)
CP = [] #initialises a checker to check when no more changes are occuring
i = 0 #Initialise the indexing for stepping through ints
i_3 = i +3


while not np.array_equal(CP,ints): #checks whether changes have occurred for any value in the array ints, if the change is to a 99 value behind the current \
                    #indexing position of i
    
    CP = ints.copy()     #resets the array of copy before any changes happen in this iteration of i from 0 to end
    print("copy:", CP)
   
    print("new loop as copy <> int, i=",i)
    
    while i_3 < len(ints):
        
        i1 = int(ints[i+1]) #resets i values for new loop of value for i. This process reads the values in the 4 block chain and assigns them (the locations) to variables
        i2 = int(ints[i+2])
        i3 = int(ints[i+3])
        
        
        if ints[i] == 1:
            ints[i3]= ints[i1] + ints[i2]
            

        elif ints[i] == 2:
            ints[i3] = ints[i1]*ints[i2]
            

        elif ints[i] == 99:
            print("99i=",i)
            
##            print('is this it?')
##            print(ints)
##            sys.exit('reached 99')
            

        i += 4
        i_3 = i+3
        
        
        print("ints", ints)
        print("copy", CP)
        print("i=", i)
        print(i_3)
    i=0
    i_3 = i+3
else:
    print("Complete")
       

        
 



        





        
        
            













