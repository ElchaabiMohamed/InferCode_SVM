import time

def countdown(n):
  i = 0 
  while i < n:
    print(n - i) 
    sleep(0.1)
    i = i + 1 
  print("LIFT OFF!")

def search(string,letter):
  if letter in string:
    return "True"
  else:
    return "False"

