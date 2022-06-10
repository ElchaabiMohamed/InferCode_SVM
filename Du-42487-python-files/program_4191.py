def countdown(num):
   import time
   i = 0
   while i < num:
      print(num - 1)
      time.sleep(0.1)
      i = i + 1
   print('LIFT OFF')
   
def search(ls,val):
   if val in ls:
      return True
   else:
      return False