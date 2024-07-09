
def find_max(numbers):
  max = numbers[0]
  i = 1
  new_Value = 0

  while i < len(numbers):
    new_Value = numbers[i]
    if max < new_Value:
      max = new_Value
    i+=1

  return max