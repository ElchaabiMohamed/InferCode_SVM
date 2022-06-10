#Part one
import time
def countdown(num):
   if num > 0:
      print(num)
      time.sleep(0.1)
      countdown(num-1)
   else:
      print("LIFT OFF!")

#Part two
def search(str,letter):
   i = 0
   while i < len(str):
      if str[i] == letter:
         return True
      i = i + 1
   return False

#Part three
def index(str,letter):
   i = 0 
   while i < len(str):
      if str[i] == letter:
         return i 
      else:
         return "-1"
      
#Part four
def fibonacci(n):
   if n == 0:
      return 0
   elif n == 1:
      return 1
   else:
      return fibonacci(n-1) + fibonacci(n-2)


#Part one
if __name__ == "__main__":
   print("calling countdown(\"num\")")
   print(countdown("num"))
   
#Part two
if __name__ == "__main__":
   print("calling search(\"str,letter\")")
   print(search("str,letter"))

   
#Part three
if __name__ == "__main__":
   print("calling index(\"str,letter\")")
   print(index("str,letter"))
   print("calling index(\"str,letter\")")
   print(index("str,letter"))
   
#Part four
if __name__ == "__main__":
   print("calling fibonacci(\"n\")")
   print(fibonacci("n"))
   