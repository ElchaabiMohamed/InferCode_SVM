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
    return search(string[1:],letter) 


def index(string,letter,count):
  k=len(string)
  if count==k:
    return -1
  elif string[count]==letter:
    return count
  else:
   return index(string,letter,count+1)


def fibonacci(n):
  if n==0:
    return 0
  elif n==1:
    return 1
  else:
    return fibonacci(n-2)+fibonacci(n-1)
  

