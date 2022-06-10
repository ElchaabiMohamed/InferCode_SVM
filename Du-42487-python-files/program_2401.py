import time
n = 0
def countdown(num):
   while num > n:
      print(num)
      time.sleep(0.1)
      num = num - 1
      if num == 0:
         print("LIFT OFF !")
      
   
