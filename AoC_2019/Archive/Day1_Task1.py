with open('C:/Users/kriti/Documents/Learning Python/AdventOfCode/2019/TaskOneData.txt','r') as f:

    data = list(map(float, f))

    TotalFuel = 0
    
    for i in range(len(data)):
        M = data[i]
        fuel = round((M/3)-0.4999) - 2
        TotalFuel += fuel
                   

    print(TotalFuel)
    print(data[2])
    print(round((data[2]/3)-0.5) - 2)
    
    print (round(3.0-0.5))
    
##for i in range(len(data)):
##    M = data[i]
