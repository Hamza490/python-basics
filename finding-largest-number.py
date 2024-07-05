numbers = [1, 9, 22, 44, 89, 456, 7890]
max = numbers[0]
i = 1
new_Value = 0

while i < len(numbers):
  new_Value = numbers[i]
  if max < new_Value:
    max = new_Value
  i+=1
print(max)
