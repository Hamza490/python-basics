import math

#Assignment 1 - Ask three questions, person's name, university, gpa, then print a message concatenating all three variables.
'''
name = input('What is your name? ')
uni =input('Which university do you go to? ')
gpa = input('What is your gpa? ')

print('My name is ' + name + ' and I go to ' + uni + ' where my gpa is ' + gpa)
'''
#---------------------------------------------------------------------------------------#
'''
#Assignment 2 - Ask a user their weight and convert it to kilograms and print
weight_lb = float(input('What is your weight in pounds? '))
weight_kg = weight_lb*0.45359237
print('Your weight in kg is: ')
print(round(weight_kg, 2))
'''
#---------------------------------------------------------------------------------------#

#Assignment 3 - A user is buying a home. Ask for the cost of the home and determine how much the user has to pay as their downpayment based off of their crdit score. A good credit score is 800 and aboe.

housePrice = float(input('How much does your house cost? '))
creditScore = int(input('What is your credit score? '))
downPayment = 0.0
rate = float(0.0)

def downpaymentPercentage (credit):
  print('hi')
  rate = float(0.0)
  if credit >= 800:
    return rate == 0.1;
    print(rate)
  elif credit < 800 and credit > 0:
    return rate == 0.2;
    print(rate)
  else:
    return rate == 0.0;
    print(rate)


print(creditScore)
rate = downpaymentPercentage(creditScore)
print(rate)

