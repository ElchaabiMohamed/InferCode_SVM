import time


def countdown(num):
  if num!=0:
    print(num)
    countdown(num-1)
  else:
    print("LIFT OFF!")


def search(string,letter):
  if string == "":
    return False
  elif string[0]==letter:
    return True
  else:
    search(string[1:],letter) 

#def index(string,letter):


def fibonacci(n):
  if n==0:
    return 0
  elif n==1:
    return 1
  else:
    ans=fibonacci(n-1)+fibonacci(n-2)
  
