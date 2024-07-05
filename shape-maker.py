#Initiaize list with 5 values
numbers = [5, 2, 5, 2, 2]

for element in numbers: #For each element in the list 'numbers' 
  output = '' #initialize the output as blank
  for counter in range(element): #for each counter (starting from 0) up to the element value, add an x to the end of the string
    output += 'x'
  print(output) #Print that line, then move onto the next element and build the about once again