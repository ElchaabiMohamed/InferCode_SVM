import time


def countdown(num):
  if num!=0:
    print(num)
    countdown(num-1)
  else:
    print("LIFT OFF!")

test=0
def search(string,letter):
  if string[0]==letter:
    return True
    test=1
  else:
    search(string[1:],letter)
  if test!=1:
    return False 
 

#def index(string,letter):


#def fibonacci(n):
  

