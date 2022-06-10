import time
n = 0
def countdown(num):
   while num > 1:
      print(num)
      time.sleep(0.1)
      num = num - 1
      if num == 1:
         print("LIFT OFF !")
      
   
