import os
import numpy as np
import sys
import time
def godfather():

    t = time.time()
    with open("C:/Users/kriti/Documents/Learning Python/AdventOfCode/2019/Data/Cab1.txt") as f:
        Data1 = np.genfromtxt(f,dtype=str, delimiter = ',', )
    with open("C:/Users/kriti/Documents/Learning Python/AdventOfCode/2019/Data/Cab2.txt") as g:
        Data2 = np.genfromtxt(g, dtype = str, delimiter = ',')
    ###print ('imported data', Data1)

    def RouteTrack(D): #Defines the route function for dataset D. Enter Data1 or Data2

    ##    Start = [[0],[0]]
        CurrentX = 0
        CurrentY = 0
    ##    route_list = [ 0,0 ]
        wire_route =[(0,0)]
        #current_position = arr.array('i', [0,0])

        for x in range(len(D)):
            instruction = D[x]
            direction = instruction[0]
            distance = int(instruction[1:])

            

            if direction == 'U':
                moving_position = CurrentY
                #print ('U')
                stationary_position = CurrentX
                ###print (type(stationary_position))
                for y in range (moving_position ,moving_position+distance):
                    ###print('y=',y)
                    ###print(type(y))
                    position = [CurrentX, CurrentY+1]
                    wire_route.append (position)
                    #wire_route.append = [y]

                    CurrentX = wire_route[-1][0]
                    CurrentY = wire_route[-1][1]
                
                ###print ('current position from wire_route=', wire_route)
                #print(CurrentX,CurrentY)
                
            if direction == 'D':
                #print('D')
                moving_position = CurrentY
                stationary_position = CurrentX
                ###print (type(stationary_position))
                for y in range (moving_position - distance ,moving_position):
                    ###print('y=',y)
                    ###print(type(y))
                    position = [CurrentX, CurrentY-1]
                    wire_route.append (position)
                    #wire_route.append = [y]

                    CurrentX = wire_route[-1][0]
                    CurrentY = wire_route[-1][1]
                #print(CurrentX,CurrentY)
            if direction == 'L':
                #print('L')
                 
                moving_position = CurrentX
                ###print ('this is moving from', moving_position)
                stationary_position = CurrentY
                ###print (type(stationary_position))
                for x in range (moving_position -distance ,moving_position):
                    ###print('y=',y)
                    ###print(type(y))
                    position = [CurrentX - 1, CurrentY]
                    wire_route.append (position)
                    #wire_route.append = [y]

                    CurrentX = wire_route[-1][0]
                    CurrentY = wire_route[-1][1]
                #print(CurrentX,CurrentY)
            if direction == 'R':
                #print('R')
                moving_position = CurrentX
                ###print ('this is moving from', moving_position)
                stationary_position = CurrentY
                ###print (type(stationary_position))
                for x in range (moving_position ,moving_position+distance):
                    ###print('y=',y)
                    ###print(type(y))
                    position = [CurrentX + 1, CurrentY]
                    wire_route.append (position)
                    #wire_route.append = [y]

                    CurrentX = wire_route[-1][0]
                    CurrentY = wire_route[-1][1]
                #print(CurrentX,CurrentY)  
        return wire_route
            
                 
    R1 = RouteTrack(Data1)
    R2 = RouteTrack(Data2)

    ##    r1 = tuple([point] for point in R1)
    ##    r2 = tuple([point] for point in R2)
    ##    print(R2)
     
            
    r1 = set(map(tuple,R1))
    r2 = set(map(tuple,R2))

    intersections = r1.intersection(r2)
        #print('lolllll',intersections)

    positive_vals = [(abs(i[0]), abs(i[1])) for i in intersections]
        #print (positive_vals)
             
        #absolute_vals = [(abs(intersections[0]), abs(intersections[1])) for i in intersections]

    distances = [sum(i) for i in positive_vals]
    distances.remove(0)
        #print(distances)
    print(min(distances))
    
    
                        #####PART 2#####
        #we want to sum the distance vecotr of the path up to each intersection, for each route, then add the two together
    def steps(route, intersections):

        #print(route, intersections)
        
        listup = [', '.join(map(str, x)) for x in intersections]
        print(listup)
        listup.remove('0, 0')
        #print('LISTUPPPPPPP',listup, type(listup[1]))
        #print('LISSSSTTT', route)
        #route_str = [str(route[x])for x in route]
        print(listup[0])
        print(str(route[1]))
        stroute = [str(route[i]) for i in range(len(route))]
        #print(stroute)
        
        #print(route_str)
        pos_int = [stroute.index('['+i+']') for i in listup]
        print(pos_int)
        print(type(pos_int[0]))
        return pos_int

    pos_int_1 = steps(R1, intersections)
    pos_int_2 = steps(R2, intersections)

    steps_toreach_int = [pos_int_1[i] + pos_int_2[i] for i in range(len(pos_int_1))]
    #steps_toreach_int.remove(4)
    print('lollllllll',min(steps_toreach_int))
        



    print(time.time() - t)

    #total_distance = steps(R1) + steps(R2)
    #print(min(total_distance)+2)

    
    #steps(R1, intersections)
godfather()










