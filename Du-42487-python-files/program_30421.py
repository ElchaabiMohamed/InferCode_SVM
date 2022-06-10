def get_price(age):
   if age <= 16:
      return 5
   if age > 60:
      return 7
   else:
      return 10

def merge_lists(l1,l2):
   l3 = l1[0::2] + l2[0::2]
   return l3

def weird_case(some_str):
   s1 = some_str[1::3].lower()
   s2 = some_str[0::2].upper()
   s3 = s1 + s2
   return s3

def remove_zeros(list):
   i = 0
   while i < len(list):
      if 0 in list:
         list.remove(0)
      i = i + 1


   
    
   
   
