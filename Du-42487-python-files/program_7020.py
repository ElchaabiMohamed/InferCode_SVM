def countdown(num):
   import time
   i=0
   while i < num:
      print(num-i)
      time.sleep(0.1)
      i=i+1
   print('LIFT OFF!')     
    
def search(str,letter):
   if letter in str:
      return 'True'
   else:
      return 'False'    
      
def index(str,letter):
   if letter in str:
      pos=str.index(letter)
      return pos
   else:
      return '-1'
         
def fibonacci(n):
   fib=[0,1,1,2,3,5,8,13,21,34]
   if n==0:
      num=fib[0]
   elif n==1:
      num=fib[1]
   else:
      num=fib[n-1]+fib[n-2]
   return num
    
if __name__ == '__main__':
   print(fibonacci(0))
      





   