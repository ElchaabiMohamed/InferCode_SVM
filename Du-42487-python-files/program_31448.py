def countdown(num):
  import time
  while num > 0:
    print(num) 
    time.sleep(0.1)
    num -= 1
  print("LIFT OFF!")

def search(str, letter):
  if letter in str:
    return "True".rstrip()
  else:
    return "False".rstrip()

def index(str, letter):
  return str.find(letter)

def fibonacci(n):
  a = 1
  b = 1
  for i in range(n-1):
    a,b = b, a+b
  return a
