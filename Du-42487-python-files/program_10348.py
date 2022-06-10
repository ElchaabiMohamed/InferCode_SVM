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
   new_str = some_str[0::2].isalpha()
   return new_str

