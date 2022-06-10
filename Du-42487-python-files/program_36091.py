def get_price(age):
   age = int(age)

   if age <= 16:
      return "5"

   elif age > 60:
      return "7"

   else:
      return "10"

def merge_lists (l1,l2):
   list = []

   i = 0
   while i < len(l1):
      list.append(l1[i])
      i += 2

   i = 0
   while i < len(l2):
      list.append(l2[i])
      i += 2
   
   return list

def weird_case(some_str):
   some_str = some_str.lower()
   sentence = list(some_str).split()

   i = 0
   while i < len(sentence):
      if sentence[i].isalpha() and i%2 == 0:
         sentence[i] = sentence[i].upper()
         i = i + 1
      i = i + 1

   return sentence

def remove_zeros(list):
   i = 0
   while i < len(list):
      if list[i] == 0:
         list.remove(list[i])
      i += 1
