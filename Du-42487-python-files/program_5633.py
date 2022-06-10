import sys, time
def countdown(num):
  if num == 0:
    print("LIFT OFF!")
    return
  time.sleep(0.1)
  print(num)
  countdown(num-1)

def search(s,letter):
  return letter in s
  

def index(s,letter, num):
  if num == len(s):

    return -1
  if s[num] == letter:
 
    return num
  index(s, letter, num + 1)
  

def fibonacci(n):
  if n == 0: 
     return 0
  a,b = 1,1
  for i in range(n-1):
    a,b = b,a+b
  return a 

