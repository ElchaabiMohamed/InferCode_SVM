def get_price(age):
   if int(age) <= 16:
      print("5")
   elif int(age) >= 60:
      print("7")
   else:
      print("10")
	  
	  
def merge_lists(l1, l2):
   merged_list = []
   i = 0
   while i < len(l1):
      merged_list.append(l1[i])
      i = i + 2
   i = 0
   while i < len(l2):
      merged_list.append(l2[i])
      i += 2
   print(merged_list)