import time


def countdown(num):
  if num!=0:
    print(num)
    countdown(num-1)
  else:
    print("LIFT OFF!")


def search(string,*letter):
  i=0
  if string[i]==letter[0]:
    return True
  else:
    count=i+1
    search(string[count],letter[0])



#def index(string,letter):


#def fibonacci(n):


