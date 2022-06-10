import time


def countdown(num):
  i=num
  while i>0:
    print(i)
    time.sleep(0.1)
    i=i-1
  print("LIFT OFF!")

def search(string,letter):
  i=0
  if letter in string:
    return True
  else:
    return False
