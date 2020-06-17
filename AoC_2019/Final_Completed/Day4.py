import os
import numpy
import math
import time
from ttictoc import tic,toc

def password_cracker (type):
    tic()
    condition_1 = []
    condition_2 = []
    p_range = range(272092, 815432)
    
    def Cond_1():
        
        for i in p_range:
            dx = [str(i)[x] for x in range(0,6)]
            #print(dx)
                                                    #This commented out block worked, but I did not like the long length and it seemed quite clunky#
##            for x in range(len(p_range)):
##            if ((dx[0] == dx[1]) and (dx[1] != dx[2])) or ((dx[0] != dx[1]) and (dx[1] == dx[2]) and (dx[2] != dx[3])) or ((dx[1] != dx[2]) and(dx[2] == dx[3]) and (dx[3] != dx[4])) or ((dx[2] != dx[3])and (dx[3] == dx[4]) and (dx[4] != dx[5])) or ((dx[3] != dx[4]) and (dx[4] == dx[5])) :
##                condition_1.append(i)

                                                    #This next block was used to replace the long line seen above. Still hard-coded in a way, but it works and looks a but nicer#
            if ((dx[0] == dx[1]) and (dx[1] != dx[2])):
                condition_1.append(i)
            for ix in range(1,4):
                if (dx[ix-1] != dx[ix]) and (dx[ix] == dx[ix+1]) and (dx[ix+1]!=dx[ix+2]):
                    condition_1.append(i)
            if ((dx[3] != dx[4]) and (dx[4] == dx[5])):
                condition_1.append(i)

        return condition_1
            
    def Cond_2():
        for i in p_range:
            dx = [str(i)[x] for x in range (0,6)]
            if dx[0] <= dx[1] and dx[1]<= dx[2] and dx[2]<= dx[3] and dx[3]<=dx[4] and dx[4]<= dx[5]:
                condition_2.append(i)
        return condition_2

            
##    for i in range(101,121):
##        for x in range(0,3):
##            d_x = str(i)[x]
##            print(dx)   


    def numcon_1 ():
        for i in p_range:
            dx = [ i//10**n % 10 for n in range(0,6)]
            if ((dx[0] == dx[1]) and (dx[1] != dx[2])):
                condition_1.append(i)
            for ix in range(1,4):
                if (dx[ix-1] != dx[ix]) and (dx[ix] == dx[ix+1]) and (dx[ix+1]!=dx[ix+2]):
                    condition_1.append(i)
            if ((dx[3] != dx[4]) and (dx[4] == dx[5])):
                condition_1.append(i)
        return condition_1
        print(dx)    
    def numcon_2():
        for i in p_range:
            dx = [ i//10**n % 10 for n in range(0,6)]
##            for y in range(0,5):
##                if dx[y] > dx[y+1]:
##                    continue
##                else:
##                    condition_2.append(i)
            if dx[0] >= dx[1] and dx[1]>= dx[2] and dx[2]>= dx[3] and dx[3]>=dx[4] and dx[4]>= dx[5]: # Minor difference here is that the number method gets the number seperated in reverse order when n goes from 0 to 5, so need to reverse the inequalities
                condition_2.append(i)
        return condition_2

            
        


    if type == 'num':
        both_conditions = set(numcon_1()) & set(numcon_2()) #Here, can use either numcon_X or Cond_X, one uses strings the other numerical methods to compare the digits
    if type =='str':
        both_conditions = set(Cond_1()) & set(Cond_2())
    print(len(both_conditions))
    #print(both_conditions)
    elapsed = toc()
    print (elapsed)
    return elapsed
##    if (5+4 == 9 and 12+7 != 19) or (5+4 ==10 and 12+7 ==19) or (5+4 ==9 and 12+7==19):     # Troubleshooting#
##        print ('yes')
time_num = password_cracker('num')  
time_str =password_cracker('str')
print('Using the string method is ', (time_num - time_str)/time_num*100, '% faster than the number method') 

                                    # A neater way to seperate digits in a large number was found after the task was completed. Divides by a power of 10**n /
                                    #which moves the required digit to the single unit position. The % then returns the remainded when dividing by the power of 10 to return the single digit
                                    # This method uses 0 indexing and starts from the RIGHT of the number 
##def get_digit(number, n):
##    return number // 10**n % 10
##
##get_digit(987654321, 0)
### 1
##
##get_digit(987654321, 5)
### 6
# It is probably more efficient to use this method. NO! After doing a tictoc of it, it is seen that the string converting method is actually more efficient! By 1.5 seconds! Maybe something to do with the loops?

