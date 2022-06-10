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
#get this one working
def index(steve,letter,n):
    if letter != steve[n]:
       index(steve,letter,n + 1)
    else:
       return n
     
#why does this script work on einsten but give me recursion limit error locally...
def fibonacci(n):
   l = []
   if n <= 1:
      return n
   else:
      return fibonacci(n - 1) + fibonacci(n - 2)
