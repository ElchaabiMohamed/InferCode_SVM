import time
def countdown(x):
   print(x)
   while x != 0: 
      time.sleep(0.1)
      x = x - 1
      print(x)
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
      
 
