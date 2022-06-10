def get_price(age):
   if age < 16:
      return '5'
   elif age > 60:
      return '7'
   else:
      return '10'
	  
def merge_lists(l1,l2):
   list3 = []
   i = 0
   while i < len(l1):
      if i % 2 == 0:
         list3.append(l1[i])
      i = i + 1
	  
   k = 0
   while k < len(l2):
      if k % 2 == 0:
         list3.append(l2[k])
      k = k + 1