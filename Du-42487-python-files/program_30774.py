def get_price(age):
   if age <= 16:
      return "5"
   elif age > 60:
      return "7"
   else:
      return "10"

def merge_lists(l1,l2):
   l3 = []
   i = 0
   while i < len(l1):
      l3.append(l1[i])
      i = i + 2
   i = 0
   while i < len(l2):
      l3.append(l2[i])
      i = i + 2
   return l3

def weird_case(string):
   i = True
   string1 = " "
   for char in string:
      if i:
         string1 += char.upper()
      else:
         string1 += char.lower()
      if char != ' ':
         i = not i
         
   

def remove_zeros(list):
    i = 0
    while i < len(list):
       if 0 in list:
           list.pop(0)
       i = i + 1



if __name__ == '__main__':
   print('calling weird_case(\'change the case\')')
   print(weird_case('change the case'))

