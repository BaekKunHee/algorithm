def find_max_num(array):
  max_number = array[0]
  for number in array:
    if number > max_number:
      max_number = number
  return max_number

print(find_max_num([3, 29, 38, 12, 57, 74, 40, 85, 61]))