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
    i = 0
    a = some_str
    l = []
    for word in a:
        if i:
           l.append(word.upper()[::2]) 
        i = int(not i)
    return "".join(l)

#cHaNge ThE CaSe
#ChAnGe ThE cAsE
#101010 101 0101
