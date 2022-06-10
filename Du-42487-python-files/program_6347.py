def countdown(num):
   import time
   i = 0
   while i < int(num):
      print(int(num) - i)
      time.sleep(0.1)
      i = i + 1
   print('LIFT OFF')
   
def search(ls,val):
   if val in ls:
      return True
   else:
      return False
	  
def index(string,letter):
   pos = -1
   i = 0
   while i < len(string):
      if string[i] == letter:
         pos = i
      i = i + 1
   return pos
   
def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)