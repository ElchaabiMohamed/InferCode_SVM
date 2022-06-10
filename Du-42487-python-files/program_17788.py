def get_price(age):
   if age <= 16:
      return "pay 5 euro"
   elif age > 60:
      return "pay 7 euro"
   else:
      return "pay 10 euro"

def merge_lists(l1,l2):
   l3 = l1[::2] + l2[::2]
   return l3


   
