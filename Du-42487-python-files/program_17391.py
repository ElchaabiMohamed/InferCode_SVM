import time
def countdown(x):
   print(x)
   while x != 0: 
      time.sleep(0.1)
      x = x - 1
      if x != 0:
         print(x)
   time.sleep(0.1)
   print("LIFT OFF!")
 
def search(string,letter):
   if letter not in string:
      return "False"
   else:
      return "True"

def index(string,letter):
   i = 0
   a = []
   while i < len(string):
      a.append(string[i])
      if string[i] == letter:
         return i
      i = i + 1
   if letter not in a:
      return "-1"

def fibonacci(n):
   list = [0]
   i = 0
   while n >= len(list):
      if len(list) > 1:
         new = list[i] + list[i-1]
      else:
         new = list[i] + 1 
      list.append(new)
      i = i + 1
   return list[-1]