user_input = input().lower()
status = ""

while user_input != 'quit':
  if user_input == 'help':
    print("""
start - to start the car
stop - to stop the car
quit - to exit       
    """)                       
  elif user_input == 'start':
    print("Car has started...We're ready to go!")
  elif user_input == 'stop':
    print("Your car has stopped. Nice breaking )")
  else:
    print("Sorry, I don't understand. Retype your command.")

  user_input = input()

print('Thank you for playing my game.')