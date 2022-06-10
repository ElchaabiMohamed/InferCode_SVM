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
   new = ''
   i = True
   for letter in some_str:
      if i:
         new += letter.upper()
      else:
         new += letter.lower()
      if letter != ' ':
         i = not i 
      return new
   
   
def remove_zeros(list):
   i = 0
   while i < len(list):
      if 0 in list:
         list.remove(0)
      i = i + 1


   
    
   
   
