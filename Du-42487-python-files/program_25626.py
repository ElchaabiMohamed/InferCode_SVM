import time
def countdown(num):
   while num >= 1:
      print(num)
      num = num - 1
      time.sleep(0.1)
   print("LIFT OFF!")
   
def search(str,letter):
   for item in str:
      if item == letter:
         return True
   return False

def index(str,letter):
   i = 0

   if letter in str:
      c = letter[0]
      for ch in str:
         if ch == c:
            if str[i:i+len(letter)] == letter:
               return i
         i += 1
   return - 1

def fibonacci(n):
    if n == 0: 
       return 0
    elif n == 1: 
       return 1
    else: 
       return fibonacci(n-1) + fibonacci(n-2)
