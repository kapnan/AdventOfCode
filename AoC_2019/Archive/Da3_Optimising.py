import cmath
import math
import numpy as np
import os
import sys



def data_track():
    #print('wtf')
    
    with open("C:/Users/kriti/Documents/Learning Python/AdventOfCode/2019/Data/Cab1.txt") as f:
        Data1 = np.genfromtxt(f,dtype=str, delimiter = ',', )
    #print (len(Data1))
    with open("C:/Users/kriti/Documents/Learning Python/AdventOfCode/2019/Data/Cab2.txt") as g:
        Data2 = np.genfromtxt(g, dtype = str, delimiter = ',')
    #print ('derp')   
    

    #print('here_1')
    #return Data1, Data2

    def routes(D):
        #print('here')
        trans = { 'U' : 1, 'D' : -1, 'L' : 1j, 'R' : -1j}

        travel = [0 + 0j]

        for i in range(len(D)):
            instruction = D[i]
            direction = instruction[0]
            dist = int(instruction[1:])
            for co in range(dist):
                
                new_p = travel[-1] + trans[direction]
                travel.append(new_p)

        #print (travel)
        travel.remove(0) #creates a variable for the travel exluding 0

        return travel

    R1 = routes(Data1)
    #print('hiii',R1)
    R2 = routes(Data2)
    #print('hello', R2)
    intersections = []
    
##    intersections = R1.intersection(R2)

##    x = [1,2,3,4]
##    y = [1,2,4,5,6]
##    R1 = [1+2j, 3+4j]
##    R2 = [3+4j, 1+2j]
##    print (R1)
##    for i in range(len(R1)):
##        #print(i)
##        if R1[i] in R2:
##            intersections.append(R1[i])

                            ###METHOD_1###
    intersections = set(R1) & set(R2)
    #print (intersections)
    print('Method 1)',min(abs(i.real)+abs(i.imag) for i in intersections))

                            ###METHOD_2###
##    set_1 = set(R1)
##    set_2 = set(R2)
##
##    intersections = set_1.intersection(set_2)
##
##    print('Method 2)',min([abs(i.real)+abs(i.imag) for i in intersections])) # notice the square brackets here
##                            ###METHOD_3###
##    
##    def distance(d):
##        return int(abs(d.real) +abs(d.imag))
##    
##    print('Method 3)',min([distance(i) for i in intersections]))
##                            ###METHOD_4### This was the one I was trying before, but did not know that 'for i in intersections' would work
##    DDistance = []
##    
##    for i in intersections:
##        DDistance.append(abs(i.real)+abs(i.imag))
##    print('Method 4)',min(DDistance))
    
    #                           #####PART_2#####
    #we want to sum the dist vector of the path up to each intersection, for each route, then add the two values together. Find the minimum of the combined distances to reach any intersection
    def steps_taken (Route):
        location = [] 
        for i in intersections:
            location.append(Route.index(i))
        return location
        
    index_1 = steps_taken(R1)
    index_2 = steps_taken(R2)

    

    cum_dist = [index_1[i] + index_2[i] for i in range(len(intersections))] 

    print (min(cum_dist)+2) # +2 because travel needs to start at 0, but is removed to stop intersections at 0, therefore leading to a loss of one index if not accounted for.

    #print(index_1)
    #print (R1)
                



data_track()
