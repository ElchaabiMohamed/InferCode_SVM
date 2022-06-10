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
      index = letter.index('str')
      if str[i] == letter:
         return index
      else: 
         return "-1"
      i = i + 1
      
#Part four
#def fibonacci(n):




#Part one
if __name__ == "__main__":
   print("calling countdown(\"num\")")
   print(countdown("num"))
   
#Part two
if __name__ == "__main__":
   print("calling search(\"str,letter\")")
   print(search("str,letter"))
   print("calling search(\"str,letter\")")
   print(search("str,letter"))
   s
#Part three
if __name__ == "__main__":
   print("calling index(\"str,letter,pos\")")
   print(index("str,letter,pos"))