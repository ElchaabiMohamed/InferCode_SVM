#
def get_price(age):
   if age <= "16":
      return "10"
   elif age > "60":
      return "7"
   else:
      return "10"

def merge_lists(l1,l2):
   l1 = []
   l2 = []
   l4 = l1[::2]
   l5 = l2[::2]
   l3 = l1 + l2
   return l3 
   
   
