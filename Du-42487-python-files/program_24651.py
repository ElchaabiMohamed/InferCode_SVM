import time


def countdown(num):
  i=num
  while i>0:
    print(i)
    time.sleep(0.1)
    i=i-1
  print("LIFT OFF!")

def search(string,letter):
  if letter in string:
    return True
  else:
    return False

def index(string,letter):
  i=0  
  test=-1
  while i<len(string):
    if letter == string[i]:
      test=i
    i=i+1
  return test
