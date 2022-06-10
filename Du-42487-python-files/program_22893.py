import time 

def countdown(num):
   i = 0 
   while num != 0: 
      time.sleep(0.1)
      print(num)
      num = num - 1
      i = i + 1   
   print("LIFT OFF!")

def search(str,letter):
   
   if letter in str:
      return True 
   else:
       return False   