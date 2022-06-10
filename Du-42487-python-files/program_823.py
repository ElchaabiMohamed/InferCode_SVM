import sys, time
def countdown(num):
  while num > 0:
    time.sleep(0.1) 
    return num
    num -= 1
  return "LIFT OFF!"

def search(s,letter):
  return letter in s

def index(s,letter):
  if letter in s:
    return s.index(letter)
  else: 
    return -1 

def fibonacci(n):
  if n == 0: 
     return 0
  a,b = 1,1
  for i in range(n-1):
    a,b = b,a+b
  return a 

