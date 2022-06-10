import time

def countdown(count):
 while (count >=1):
  print(count)
  time.sleep(0.1)
  count -= 1
 print ("LIFT OFF!")

if __name__ == '__main__':
   countdown(3)

def search(ls,val):
 for item in ls:
  if item == val:
    return True
 return False

def index(str,letter):
  i = 0
  while i < len(str):
   if str[i] == letter:
     return i
   i = i + 1
  return -1

def fibonacci(n):
  fib = [0,1,1]
  for f in range(2,n):
      fib.append(fib[-1]+fib[-2])
  return fib[n]
