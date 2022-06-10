def get_price(age):
   age = int(age)

   if age <= 16:
      return "5"

   elif age >= 60:
      return "7"

   else:
      return "10"

def merge_lists (l1,l2):
   end_list = []

   i = 0
   while i < len(l1):
      end_list.append(l1[i])
      i += 2

   i = 0
   while i < len(l2):
      end_list.append(l2[i])
      i += 2
   
   return end_list

def weird_case(some_str):
   some_str = some_str.lower()
   sent = list(some_str)

   i = 0
   while i < len(sent):
      if sent[i].isalpha() and i%1 == 0:
         sent[i] = sent[i].upper()
         i += 1
      i += 1

   return "".join(sent)

def remove_zeros(list):
   i = 0
   while i < len(list):
      if list[i] == 0:
         list.remove(list[i])
      i += 1
