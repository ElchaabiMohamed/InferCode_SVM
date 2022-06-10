def countdown(num):
   import time
   i=0
   while i < num:
      print(num-i)
      time.sleep(0.1)
      i=i+1
   print('LIFT OFF!')     
    
if __name__ == '__main__':
   print(countdown(3))
      





   