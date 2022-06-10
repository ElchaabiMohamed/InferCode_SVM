import sys, time
def countdown(num):
  while num > 0:
    time.sleep(0.1) 
    print(num)
    num -= 1
  print("LIFT OFF!")

def search(str,letter): 
  if letter in str:
    print(True)
  else:
    print(False)

def index(str,letter):
  if letter in str:
    print(str.index(letter))
  else: 
    print(-1) 

def fibonacci(n):
  a,b = 1,1
  for i in range(n-1):
    a,b = b,a+b
  print(a) 

