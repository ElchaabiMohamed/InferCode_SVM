#
import time


def countdown(num):
   while num > 0:
      print(num)
      num = num - 1
      if num == 0:
         time.sleep(1.0)
         print("LIFT OFF!")
 
def search(str,letter):
   if letter in str:
      return "True"
   else:
      return "False"
 

def index(str,letter):
   i = str[0]
   letter_pos = 1
   while i < len(str):
      if letter in str:
         letter_pos = i + 1
      i = i + 1
   return letter_pos


def fibonacci(n):
   if n == 0:
      return 0
   if n == 1:
      return 1 
   else:
      return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
   print('calling countdown(\'countdown num\')')
   print(countdown('countdown num'))

if __name__ == '__main__':
   print('calling search(\'search for letter\')')
   print(search('search for letter'))

if __name__ == '__main__':
   print('calling index(\'position of letter\')')
   print(index('position in letter'))

if __name__ == '__main__':
   print('calling fibonacci(\'fibonacci number\')')
   print(fibonacci('fibonacci number'))


  
  