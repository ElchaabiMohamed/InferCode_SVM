def get_price(age):
   if age <= 16:
      return "5"
   elif age < 60:
      return "10"
   elif age >= 60:
      return "7"

def merge_lists(l1,l2):
   l3 = l1[0::2] + l2[0::2]
   return l3

def weird_case(some_str):
   new_str = some_str.lower()
   return new_str.upper[0::2]

def remove_zeros(list):
   i = 0
   while i < len(list):
      if 0 in list:
         list.remove(0)
      i = i + 1

