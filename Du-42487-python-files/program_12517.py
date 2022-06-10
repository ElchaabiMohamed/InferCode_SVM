#Jennifer's Solution
def merge_lists(l1,l2):
   '''take two lists l1 and l2 and return a third list which contains 
   every second element of l1 and l2'''
   l3 = []
   i = 0
   while i < len(l1):
       l3.append(l1[i])
       i += 2
   i = 0
   while i < len(l2):
       l3.append(l2[i])
       i += 2
   return l3
 
def weird_case(some_str):
     '''takes a string some_str and contains a new string which contains 
 every second letter in some_str'''
     new_str = ""
     i = 0
     lc = 0 # separate count for the letters
     while i < len(some_str):
         if some_str[i].isalpha():
             if lc % 2 == 0:
                 new_str += some_str[i].upper()
             else:
                 new_str += some_str[i].lower()
             lc += 1
         else:
           new_str += some_str[i]
         i = i + 1
     return new_str
 
def remove_zeros(list):
     '''take a list of numbers and remove zeros from the list'''
     while 0 in list:
         list.remove(0)
 
def get_price(age):
     '''checks age and returns price associated with the age'''
     if age <= 16:
         return 5
     elif age <=60:
         return 10
     else:
         return 7