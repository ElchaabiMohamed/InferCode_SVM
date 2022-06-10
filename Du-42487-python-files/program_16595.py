import time


def countdown(num):
  if num!=0:
    print(num)
    countdown(num-1)
  else:
    print("LIFT OFF!")


def search(string,letter):
  test=0
  if string[0]==letter:
    test=1
  else:
    search(string[1:],letter)
  if test==0:
    return False 
  else:
    return True 

#def index(string,letter):


#def fibonacci(n):
  

