#Test 1
def get_price(age):
  if age <= 16:
    return "5"
  elif age > 60:
    return "7"
  else:
    return "10"

#Test 2
def merge_lists(l1,l2):
  l3 = []
  for lines in l1, l2:
    l3 = l1[::2] + l2[::2]
    return l3

#Test 3
def weird_case(some_str):
  stringy = ""
  capital = True
  for letters in some_str:
    if capital:
      stringy = stringy + letters.upper()
    else:
      stringy = stringy + letters
    if letters != " ":
      capital = not capital
  return stringy
if __name__ == '__main__':
   print('calling weird_case(\'change the case\')')
   print(weird_case('change the case'))

#Test 4
def remove_zeros(listy):
  i = 0
  for numbers in listy:
    if 0 in listy:
      listy.remove(0)
