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
   l3 = (l1[i] + 1) + (l2[i] + 1)
   return l3
   
if __name__ == "__main__":
   print("calling get_price(\"age\")")
   print(get_price("age"))
   
if __name__ == "__main__":
   print("calling merge_lists(\"l1,l2\")")
   print(merge_lists("l1,l2"))