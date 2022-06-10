import time
def countdown(x):
   print(x)
   while x != 0: 
      time.sleep(0.1)
      x = x - 1
      if x != 0:
         print(x)
   time.sleep(0.1)
   return "LIFT OFF!"

def search(string,letter):
   i = 0
   a = []
   while i < len(string):
      a.append(string[i])
      i = i + 1
   if letter not in a:
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
       
   
