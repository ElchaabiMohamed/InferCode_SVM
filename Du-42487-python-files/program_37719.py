import time

def countdown(n):
  i = 0 
  while i < n:
    print(n - i) 
    time.sleep(0.1)
    i = i + 1 
  print("LIFT OFF!")

def search(string,letter):
  i = 0
  while i < len(string):
    if string[i] == letter:
      return True
    i = i + 1
  return False

def index(string,letter):
  if letter in string:
    i = 0
    while i < len(string):
      if letter == string[i]:
        return i 
      i = i + 1 
  else:
    return "-1"

def fibonacci(n):
  a = 0
  b = 1
  for i in range(0, n):
    temp = a
    a = b
    b = temp + b
  return a