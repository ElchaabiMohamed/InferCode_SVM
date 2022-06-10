import sys, time
def countdown(num):
  while num > 0:
    time.sleep(0.1) 
    print(num)
    num -= 1
  print("LIFT OFF!")

def search(s,letter):
  print(letter in s)
''' 
  if letter in s:
    print True
  else:
    print False
'''
def index(s,letter):
  if letter in s:
    print(s.index(letter))
  else: 
    print(-1) 

def fibonacci(n):
  if n == 0: 
     return 0
  a,b = 1,1
  for i in range(n-1):
    a,b = b,a+b
  return a 

