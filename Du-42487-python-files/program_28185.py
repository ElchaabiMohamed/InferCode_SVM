def get_price(age):
  if age < 16:
    return "5"
  elif age > 60:
    return "7"
  else:
    return "10"

def merge_lists(l1,l2):
  l3 =[]
  i = 0
  while i < len(l1):
    if i % 2 == 0:
      l3.append(l1[i])
    i = i + 1
  j = 0
  while j < len(l2):
    if j % 2 == 0:
      l3.append(l2[j])
    j = j + 1
  return l3

def weird_case(some_str):
  new_str = ""
  for value in some_str:
    if value == " ":
      new_str = new_str + value
    elif value is True:
      new_str = new_str + value.upper()
    else:
      new_str = new_str + value
  return new_str

def remove_zeros(list):
  i = 0
  while i < len(list):
    if 0 in list:
      list.remove(0)
    i = i + 1

if __name__ == "__main__":
  print("calling weird_case(\"change the case\")")
  print(weird_case("change the case"))
