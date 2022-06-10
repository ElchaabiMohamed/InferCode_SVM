import time

def countdown(num):
   while num > 0:
      for n in num:
         print(num, time.sleep(0.1)) 
         num = num - 1
         if num == 0:
            print("LIFT OFF!")