#
def get_price(age):
   if age <= 16:
      return "5"
   elif age >= 60:
      return "7"
   else:
      return "10"

def merge_lists(l1,l2):
   l3 = l1[::2] + l2[::2]
   return l3

 
def weird_case(some_str):
   second = some_str   
   for some_str[::2] in some_str:
      weird = some_str.upper()[::2]
      return weird + some_str 



