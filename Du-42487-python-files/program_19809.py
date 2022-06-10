import time
#It works yay
def countdown(num):

    time.sleep(.100)
    if num > 0:
       print(num)
       countdown(num - 1)
       time.sleep(.100)

    else:
       print("LIFT OFF!")


#Round two fight....I really don't wan't to rewrite this
def search(steve,letter):
    if letter in steve:
       return True
    else:
       return False

def index(steve,letter):
     return steve.find(letter)

def fibonacci(n):
   l = []
   if n <= 1:#why does this not work if its == to 1...
      return n
   else:
      return fibonacci(n - 1) + fibonacci(n - 2)
