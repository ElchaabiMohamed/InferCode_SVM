#funky funcs

def get_price(age):
#  16s and under pay 5 euro
   if age<=16:
      return 5
#  over 60s pay 7 euro
   elif age>60:
      return 7
#  everyone else pays 10 euro
   else:
      return 10

def merge_lists(l1,l2):
#  takes two lists, l1 and l2, and returns a third list which contains every second element of l1 and l2
   l3=[]
   flip=1
   for num in l1:
      if flip>0:
          l3.append(num)
      flip=-flip
   flip=1
   for num in l2:
      if flip>0:
          l3.append(num)
      flip=-flip
   return l3

def weird_case(some_str):
#    takes a string, some_str, and returns a new string in which every second letter is uppercase
   words= some_str.split()

   flipper=1
   SoMe_StR=[]
   for word in words:
      word=list(word)
      for letter in word:
         if flipper>0:
            SoMe_StR.append(letter.upper())
         else:
            SoMe_StR.append(letter)
         flipper=-flipper
      SoMe_StR.append(" ")
      flipper=1
   return "".join(SoMe_StR)

def remove_zeros(List):
#    takes a list, list, and removes zeros. Note: nothing is returned from this function. 
   i=0
   while 0 in List:
      List.remove(0)
#############################
