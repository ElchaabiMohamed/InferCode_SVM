def get_price(age):
   if int(age) <= 16:
      price = 5
   elif int(age) > 60:
      price = 7
   else:
      price = 10
   return price
   
#def merge_lists(11,12):
 #  i = 0
  # 13 = []
   #while i < len(11):
    #  13.append(11[i])
     # i += 2
   #j = 0
   #while j < len(12):
      #13.append(12[j])
      #j += 2
      #return 13

#def weird_case(some_str):
  # new_str = ""
   #i = True
   #for letter in some_str:
    #  if i:
     #    new_str += letter.upper()
      #else:
       #  new_str += letter.lower()
      #if letter != " ":
       #  i = not i
   #return new_str
   
#def remove_zeros(list):
  # i = 0
   #while i < len(list):
    #  if 0 in list:
     #    list.remove(0)
      #i = i + 1                           
