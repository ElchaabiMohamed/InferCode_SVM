import time


def countdown(num):
  if num!=0:
    print(num)
    countdown(num-1)
  else:
    print("LIFT OFF!")

def search(string,letter):
  i=0
  if string[i]==letter:
    return True
  elif i<len(string):
    i=i+1
    search(string[i+1],letter)
  else:
    return False

#def index(string,letter):


#def fibonacci(n):


