import numpy as np
##import urllib.request
##
##link = 'https://adventofcode.com/2019/day/1/input'
##
##f = urllib.request.urlopen(link)


with open('C:/Users/kriti/Documents/Learning Python/AdventOfCode/TaskOneData.txt','r') as f:
    

    data = np.genfromtxt(f, int)

ModFuel = 0
Fuel_UnAcc = 0 #Initialising of fuel required for unaccounted fuel variable
FuelFuel = 0
for i in range(len(data)):
        M = data[i]
        fuel = round((M/3)-0.4999) - 2
        FuelMassUnAcc = fuel
        while FuelMassUnAcc >= 0 :
            Fuel_UnAcc = round((FuelMassUnAcc/3)-0.499)-2
            if Fuel_UnAcc < 0:
                break
            FuelMassUnAcc = Fuel_UnAcc # Makes the newly calculated fuel the unaccounted for mass
            FuelFuel += Fuel_UnAcc # Adds the newly accounted for fuel to a tally
            
        ModFuel += fuel

#FuelMassUnAcc = ModFuel #Fuel also has a mass which needs more fuel to be launched
                        #FuelMassUnAcc is the unaccounted for fuel mass



##while FuelMassUnAcc >= 0 :
##    Fuel_UnAcc = round((FuelMassUnAcc/3)-0.4999) - 2
##    if Fuel_UnAcc <0:
##        break
##    FuelFuel += Fuel_UnAcc #Add the unaccounted for fuel to a tally
##    FuelMassUnAcc = Fuel_UnAcc#make the new calculated fuel the unaccounted mass and loop through if mass is remaining
##    


TotalFuel = ModFuel + FuelFuel                   

print(TotalFuel)
print(data[2])
print(FuelFuel)
print(ModFuel)

    


