def get_price(age):
   if age <= 16:
      return "5"
   elif age > 60:
      return "7"
   else:
      return "10"

def merge_lists(l1,l2):
   l3 = []
   i = 0
   while i < len(l1):
      l3.append(l1[i])
      i = i + 2
   i = 0
   while i < len(l2):
      l3.append(l2[i])
      i = i + 2
   return l3

def weird_case(string):
   string = input()
   letters = string.split()
   while i < len(letters):
      if i % 2 == 0:
         print(letters[i])
      elif i % 2 != 0:
         print(letter[i].upper)
      i = i + 1

      