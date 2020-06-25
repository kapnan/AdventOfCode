# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 00:15:15 2020

@author: kriti
"""


# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 15:50:00 2020
AoC_2109 Day 6 - Attempt 1
@author: kriti
"""
with open(r"C://Users/kriti/AdventOfCode/AoC_2019/Data/Orbitals_Input.txt", "r") as f:
    orbitals = list(map(str, f))
# =============================================================================
# def mapper(searching_from, count_hist, exit_term):
#     new_list = []
#     end = 1
#     Round_count = 0
#     new_search = []
#     if exit_term in searching_from:
#         return Round_count, new_search, end
#     for p in orbitals:
#         
#         for i in searching_from:
#           
#             if p[:3] == i:
#                 Round_count += (1+count_hist)
#             
#                 if '\n' in p[-4:]:
#                     new_search.append(p[-4:].rstrip("\n"))
#                     end = 0 
#                 else:
#                     new_search.append(p[-3:])
#                     end = 0
#                     
#                 if p[-4:-1] == exit_term:
#                         print('Found:', exit_term)
#                         end = 1
#                         return Round_count, new_search, end
#                 elif p[-3:] == exit_term:
#                         print('Found:', exit_term)
#                         end = 1
#                         
# =============================================================================
            
        
                
    #dead end subtractor
# =============================================================================
#     d=0
#     for i in searching_from:
#         for p in orbitals:
#             if i in p[:3]:
#                 d=1
#         if d == 0:
#             
#             print(i,'summmmmms',sum(range(count_hist+1)) )
#             Round_count -= sum(range(count_hist+1))
#         d = 0    
# =============================================================================
    #return Round_count, new_search, end
        
def counter(searching_from, count_hist, exit_term): # if exit_term left as a space then it will be fine 
    new_list = []
    end = 1
    Round_count = 0
    new_search = []
    dist_list = [] ##part 2
    end_found = 0
    
    for p in orbitals:
        
        for i in searching_from:
          
            if p[:3] == i:
                
                if exit_term == ' ':
                    Round_count += (1+count_hist)
                elif p[-4:-1] == exit_term or p[-3:] == exit_term:
                    Round_count += (1+count_hist)
                    dist_list.append(Round_count) ##added for part 2
                    end_found = 1
                
                
                if '\n' in p[-4:]:
                    new_search.append(p[-4:].rstrip("\n"))
                    
                else:
                    new_search.append(p[-3:])
                end = 0     
            
# =============================================================================
#     if end_found == 0:
#         Round_count += 1
#         for p in orbitals: 
#             if p[-4:1] == i or p[-3:] == i:
#                 new_search.append(p[:3])
#                 end = 0
#                 return Round_count, new_search, end             
# =============================================================================
                
               
        #print (p[-4:-1], len(p[-4:]) )
# =============================================================================
#         if p[-4:-1] == exit_term:
#             end = 1
#             print('Found:', exit_term)
# =============================================================================
    if end == 1:
        ##print('None of the search for values were found, end kept as 1 and sript ended')
        end = 1       
    return Round_count, new_search, end    
    

def Orbitals(searching_from, exit_term):
    
    end = 0
    count_hist=0
    total_count = 0
    #round_count = 0
    while end == 0:
        
        Round_count, searching_from, end = counter(searching_from, count_hist, exit_term)
        
        # run counter function for the inputs in 'searching'#
        total_count += Round_count
        
        count_hist += 1
        
        ##print('orbitals NS', searching_from)
        
    ##print('Orbitals run:', total_count)
       
   
    return total_count  
print(Orbitals(['COM'], 'SAN'))
length_YOU = Orbitals(['COM'], 'YOU')     
print(Orbitals(['COM'], 'ZMN')) 

### back_stepper() finds the orbitted object (LHS) and replaces (RHS) in the searching
### list. It also adds +1 to the steps_back counter
def back_stepper(search_from, steps_back):
    
    
    for p in orbitals:
        for i in search_from:
            if p[-4:-1] == i or p[-3:] ==i:
                search_from.remove(i)
                search_from.append(p[:3])
                #print(search_from)
                ##print('backstepper complete, search from:', search_from)
                steps_back +=1 
                print('total steps back:', steps_back)
    return search_from, steps_back


search_from = ['YOU'] #can make this a user input in the future
destination = 'SAN'
steps_back = 0  #number of backwards steps taken from origin 
results_stepsback = []
results_totalsteps = []
while Orbitals(search_from, destination) == 0:
#while steps_back < length_YOU: 
    ##print('omw back yo')
    
    x = back_stepper(search_from, steps_back)
    steps_back = x[1]
    if Orbitals(x[0], destination) != 0:
        results_stepsback.append(x[1])
        results_totalsteps.append(Orbitals(x[0], destination))
        ##print ('x is: ', x)
#print(Orbitals(search_from, 'SAN') + steps_back - 2)    
    #print('drumroll',Orbitals(back_stepper(search_from)[0], 'SAN')+back_stepper(search_from)[1])
results = [a + b -2 for a in results_stepsback for b in results_totalsteps]    
#print (x)
##print (min(results))
print(results)    

#print(Orbitals(back_stepper(search_from)[0], counter, 'SAN') + back_stepper(search_from)[1])
# =============================================================================
# bc = 1
# step_back = 0
# while bc <= Orbitals(['COM'], counter, 'YOU'):
#     while step_back in range(0,bc):
#         step_back += 1
#         for p in orbitals:
#             for i in searching_from:
#                 if p[-4:-1] == i or p[-3:] == i:
#                     new_start = p[:3]
#                     
# =============================================================================
    
    
#Orbitals(['YOU'], mapper, 'SAN')
