def countdown(num=3):
   while num!=0:
      print(num)
      num=num-1
   print("LIFT OFF!")

def search(str, letter):
   if letter in str:
      print("True")
   else:
      print("False")

def index(str, letter):
   if letter not in str:
      print(-1)
   else:
      i=0
      while str[i]!=letter:
         i=i+1
      print(i)