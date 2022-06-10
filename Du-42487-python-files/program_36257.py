import time 
def countdown(num):
   if num == 0:
      print('LIFT OFF!')
   else:
      print(num)
      time.sleep(0.1)
      countdown(num -1)

def search(ls, val):
   if ls == []:
      return 
   elif ls[0] == val:
      return True
   else:
      return search(ls[1:], val)

def index(str, letter):
   if ls == []: 
      return -1
   elif ls[0] == val:
      return val
   else:
      return search(ls[1:], val)

def fibonacci(n):
   if n == 0: 
      return 0
   elif n == 1: 
      return 1
   else: 
      return fibonacci(n-1) + fibonacci(n-2)
