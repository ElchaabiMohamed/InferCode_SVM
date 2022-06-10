import time
def countdown(num):
   i = 0
   while num > 0: 
      print(num)
      time.sleep(0.1)
      num = num - 1
      if num == 0:
         print("LIFT OFF!")

def search(str,letter):
   if letter in str:
      print(True)
   if letter not in str:
      print(False)
