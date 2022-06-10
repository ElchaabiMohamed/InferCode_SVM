def get_price(age):
   if age <= 16:
      return 5
   elif age > 60:
      return 7
   else:
      return 10

def merge_lists(l1,l2):
   l3=[]
   merge = 1
   for num in l1:
      if merge > 0:
          l3.append(num)
      merge = -merge
   flip = 1
   for num in l2:
      if merge > 0:
          l3.append(num)
      merge = -merge
   return l3

def weird_case(some_str):

   words = some_str.split()
   string = 1
   some_str = []
   for word in words:
      word = list(word)
      for letter in word:
         if string > 0:
            some_str.append(letter.upper())
         else:
            some_str.append(letter)
         string =-string
      some_str.append(" ")
      string = string
   some_str="".join(SoMe_StR[:-1])
   return some_str

def remove_zeros(list):
   i = 0
   while 0 in List:
      list.remove(0)