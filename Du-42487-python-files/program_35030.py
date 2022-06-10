#
def get_price(age):
   if age <= 16:
      return "5"
   elif age >= 60:
      return "7"
   else:
      return "10"

def merge_lists(l1,l2):
   l3 = l1[::2] + l2[::2]
   return l3

 
def weird_case(some_str):
   some_str = some_str.split().upper()
   i = 0
   while i < len(some_str):
      return some_str    









   i = 0                   #going through every word
   a = some_str.split(" ") # splitting each word in sentence
   l = []                  # list
   for word in a:          #for every word in the splitted words
      if i:                # if i 
         l.append(word.upper()) #put every upper case word in list
      else:
         l.append(word)         # else put every normal word in list
      i = int(not i)            # and i is integer not
   return " ".join(l)


