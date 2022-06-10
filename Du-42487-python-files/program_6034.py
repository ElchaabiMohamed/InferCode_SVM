#!/usr/bin/env python

#Function 1:
def get_price(age):
   if age <= 16:
      return "5"
   elif age >= 60:
      return "7"
   else:
      return "10"
      
#Function 2:
def merge_lists(l1,l2):
   i = 0
   l3 = l1[::2] + l2[::2]
   return l3
   
#Function 3:
def weird_case(some_str):
   i = True
   letter = ""
   for char in some_str:
      if i:
         letter = letter + char.upper()
      else:
         letter = letter + char.lower()
      if char != " ":
         i = not i
   return letter
   
#Function 4:
def remove_zeros(list):
   if "0" in list:
      return list.remove("0")
   else:
      return list

   
if __name__ == "__main__":
   print("calling get_price(\"age\")")
   print(get_price("age"))
   
if __name__ == "__main__":
   print("calling merge_lists(\"l1,l2\")")
   print(merge_lists("l1,l2"))
   
if __name__ == "__main__":
   print("calling weird_case(\"some_str\")")
   print(weird_case("some_str"))
   
if __name__ == "__main__":
   print("calling remove_zeros(\"list\")")
   print(remove_zeros("list"))