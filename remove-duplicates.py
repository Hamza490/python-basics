list = [2, 2, 4, 6, 3, 4, 6, 1]
unique_values = []

for element in list:
  if element not in unique_values:
    unique_values.append(element)

print(unique_values)