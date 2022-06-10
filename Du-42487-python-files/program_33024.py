import time


def countdown(num):
  if num!=0:
    print(num)
    countdown(num-1)
  else:
    print("LIFT OFF!")


def search(string,letter,pos):
  if pos == len(string):
    return False
  elif string[pos]==letter:
    return True
  else:
    search(string,letter,pos+1) 

#def index(string,letter):


#def fibonacci(n):
  

