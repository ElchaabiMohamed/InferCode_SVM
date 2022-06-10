import time 

def countdown(num):
   i = 0 
   while num != 0: 
      time.sleep(0.1)
      print(num)
      num = num - 1
      i = i + 1   
   print("LIFT OFF!")

def search(letter):
   str = input()
   if letter in str:
      print(True) 
   else:
       print(false)   