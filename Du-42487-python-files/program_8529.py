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
  test=1
  while i<len(string):
    if letter==string[i]:
      return True
      test=2
    i=i+1
  if test==1:
    return False

def index(string,letter):
  i=0  
  test=-1
  while i<len(string):
    if letter == string[i]:
      test=i
    i=i+1
  return test

def fibonacci(n):
  i=0
  num=1
  num1=1
  num2=1
  while i<n:
    if n==0:
      return 0
    elif n==1:
      return 1
    num=num3+num2
    num2=num3
    num3=num
    i=i+1

  if n!=0 and n!=1:
    return num
