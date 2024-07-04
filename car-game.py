user_input = input().lower()
status = ""

while True:

  if user_input == 'help':
    status = 'help'
    print("""
start - to start the car
stop - to stop the car
quit - to exit       
    """)           

  elif user_input == 'start':
    status = 'start'
    print("Car has started...We're ready to go!")
  
  elif user_input == 'stop':
    status = 'stop'
    print("Your car has stopped. Nice breaking )")
  
  elif user_input == 'quit':
    break
  
  else:
    print("Sorry, I don't understand. Retype your command.")

  user_input = input().lower()
  while status == user_input:
    if status == 'start':
      print('Car is already started. Input a different command.')
      user_input = input().lower()
    elif status == 'stop':
      print('Car is already stopped. Input a different command.')
      user_input = input().lower()

print('Thank you for playing my game.')

#Note: the status logic can be done with a do-while loop, and boolean, where there is a nested if/else if under the start and stop if/else if checking for the boolean status before printing the result.
