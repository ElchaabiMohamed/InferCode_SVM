#

import time 
def countdown(num):
   while num >= 1:
      print (num)
      num = num - 1 
      if num == 0:
         time.sleep(1.0)
         print("LIFT OFF!")
 

def search(str, letter):
   i = 0
   while i < len(str):
      if str[i] == letter:
         return "True"
      i = i + 1 
   return "False"


def index(str,letter,pos):
   if pos == len(str):
	   return "False"
   elif str[pos] == letter:
      return "True"
   else:
      return index(str,letter,pos+1)


def fibonacci(n):
   a, b = 0, 1 
   for i in range(n):
      a, b = b,  a + b
   return a 
      
if __name__ == '__main__':
   print('testing countdown')
   countdown(10)

   print('testing search')
   print(search('test','t'))
   print(search('test','a'))
  
   print('testing index')
   print(index('test','t',0))
   print(index('test','a',0))

   print('testing fibonacci')
   print(fibonacci(5))