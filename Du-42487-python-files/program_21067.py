import time
def countdown(num):
   i = num
   while i >= 1:
      print(i)
      time.sleep(0.10)
      i = i - 1
   print('LIFT OFF!')
   return i    
   
def search(str,letter):
   if letter in str:
      return True
   else:
      return False

def index(str,letter):
   i = 0
   while i < len(str):
      if letter in str:
         return i
      else:
         return '-1'	  