def countdown(num):
   import time
   if num == 0:
      print('LIFT OFF!')
   else:
      print(num)
      time.sleep(0.1)
      countdown(num-1)
	  
def search(ls,val):
   if ls == '':
      return 'False'
   elif ls [0] == val:
      return 'True'
   else:
      return search(ls[1:],val)
	  
def index(string,letter,rv):
   if string == '':
        return -1
   elif string[0] == letter:
      return rv
   else:
      rv = rv + 1
      return index(string[1:],letter,rv)
	   
def fibonacci(n):
   if n==1 or n==2:
      return 1
   return fibonacci(n-1)+fibonacci(n-2)
