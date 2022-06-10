def get_price(age):
   if int(age) <= 16:
      return "5"
   elif int(age) >= 60:
      return "7"
   else:
      return "10"
	  
	  
def merge_lists(l1, l2):
   import sys
   merged_list = []
   i = 0
   while i < len(l1):
      merged_list.append(l1[i])
      i = i + 2
   i = 0
   while i < len(l2):
      merged_list.append(l2[i])
      i += 2
   return merged_list


def weird_case(some_str):
   i = 0
   j = 0
   new_str = ""
   while i < len(some_str):
      if some_str[i].isalpha():
         if j % 2 == 0:
            new_str += some_str[i].upper()
         else:
            new_str += some_str[i].lower()
         j += 1
      else:
         new_str += some_str[i]
      i += 1 
   return new_str

def remove_zeros(list):
   '''take a list of numbers and remove zeros from the list'''
   while 0 in list:
      list.remove(0)
