prices = []
user_choice = ''
status = True
i = 0
sum = 0

while status:
  prices.append(input('Enter price: '))
  print('Do you want to continue adding items? y/n')
  user_choice = input().lower()
  if user_choice == 'y':
    status = True
  elif user_choice == 'n':
    status = False

for item in prices:
  sum += int(prices[i])
  i+=1

print(f"Total is: {sum}")