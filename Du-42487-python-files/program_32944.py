import time
def countdown(num):
   i = num
   while i >= 1:
      print(i)
      time.sleep(0.10)
      i = i - 1
   print('LIFT OFF!')
   return i    
