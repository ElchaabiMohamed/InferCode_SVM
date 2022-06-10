import time

def countdown(n):
  i = 0 
  while i < n:
    print(n - i) 
    time.sleep(0.1)
    i = i + 1 
  print("LIFT OFF!")

def search(string,letter):
  if letter in string:
    return "True"
  else:
    return "False"

def index(string,letter):
  if letter in string:
    i = 0
    while i < len(string):
      if letter == string[i]:
        print(i) 
      i = i + 1 
  else:
    return "-1"