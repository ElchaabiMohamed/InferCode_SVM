import time


def countdown(num):
  if num!=0:
    print(num)
    countdown(num-1)
  else:
    print("LIFT OFF!")

def search(string,letter):
  if 'i' not in locals(): 
    i=0
  if string[i]==letter:
    return True
  elif i<len(string):
    search(string[i+1],letter)



#def index(string,letter):


#def fibonacci(n):


