# ASCII CODE
# ord('a') == 97
# chr(97) == 'a'

def find_max_occurence_alphabet(string):
  alphabet_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

  max_occurrence = 0
  max_alphabet = alphabet_array[0]

  for alphabet in alphabet_array:
    occurrence = 0
    for char in string:
      if char == alphabet:
        occurrence += 1
   
    if occurrence > max_occurrence:
      max_alphabet = alphabet
      max_occurrence = occurrence

  return max_alphabet

def find_max_occurence_alphabet_2(string):
  alphabet_occurrence_array = [0] * 26
  
  for char in string:
    if not char.isalpha():
      continue
    array_index = ord(char) - ord('a') # 해당 문자를 인덱스로 변환
    alphabet_occurrence_array[array_index] += 1 # 빈도수 배열에 인덱스로 찾아가서 빈도수 증가
  
  max_occurrence = 0
  max_alphabet_index = 0

  for index in range(len(alphabet_occurrence_array)):
    alphabet_occurrence = alphabet_occurrence_array[index]

    if alphabet_occurrence > max_occurrence:
      max_occurrence = alphabet_occurrence
      max_alphabet_index = index
    print('max_alphabet_index: ', max_alphabet_index)

    return chr(max_alphabet_index + ord('a'))

    # 8 -> i 인덱스 아스키 코드 형태 -> 알파벳





def find_alphabet_occurrence_array(string):
  alphabet_occurrence_array = [0] * 26
  for char in string:
    if not char.isalpha():
      continue
    arr_index = ord(char) - ord('a')
    alphabet_occurrence_array[arr_index] += 1
  return alphabet_occurrence_array

print(find_alphabet_occurrence_array("hello my name is sparta"))


print(find_max_occurence_alphabet_2("hello my name is sparta"))