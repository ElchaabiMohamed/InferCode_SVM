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
   i = 0
   while i < len(some_str):
         word = some_str.split()
         for word[::2] in some_str:
            upper_case = word.upper()




