def countdown(num):
   import time

   if num == 1:
      print(num)
      time.slep(0.1)
      countdown(num -1)

if __name__ == "__main__":
   print("Calling countdown function.")
   countdown(3)

def search (str, letter):
   if str == "":
      return False
   elif str[0] == letter:
      return True
   else:
      return search(str[1:], letter)

if __name__ == "__main__":
   print("calling search function")
   print(search ("test", "e"))
   print(search ("test", "e"))

def index(str, letter, pos):
   import fibonacci
   if pos == len(str):
      return -1
   elif str[pos] == letter:
      return pos
   else:
      return fibonacci(n -1) + fibonacci(n-2)

if __name__ == "__main__":
   print("calling fibonacci function")
   print(fibonacci(0))
   print(fibonacci(6))
