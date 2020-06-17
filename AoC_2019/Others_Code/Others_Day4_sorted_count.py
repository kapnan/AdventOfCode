potentials = []
for i in range(278384,824796): 
    potentials.append(str(i))

passedfirst = []
for item in potentials:
    if list(item) == sorted(item):
        passedfirst.append(item)
                
passedsecond = []
for number in passedfirst:
    
    for digit in number:
            count = number.count(digit)
            if count >= 2: #change this to '==' for part 2 (srsly)
                passedsecond.append(number)               
                break  

print(len(passedsecond))
