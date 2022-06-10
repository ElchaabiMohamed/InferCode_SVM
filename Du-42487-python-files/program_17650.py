import time

def countdown(count):
    while (count >= 1):
        print(count) 
        time.sleep(0.1)
        count -= 1
    print ("LIFT OFF!")

if __name__ == '__main__':
   countdown(3)


def search(str,letter):
   i = 0
   while i < len(str):
      if str[i] == letter:
        return True
      i += 1
   return False

if __name__ == '__main__':
   search(n)


def index(str,letter):
   i = 0
   while i < len(str):
      if str[i] == letter:
        return i
      i += 1
   return - 1    
 
if __name__ == '__main__':
   index(n)


def fibonacci(n):
  fib = [0,1,1]
  for f in range(2,n):
      fib.append(fib[-1]+fib[-2])
  return fib[n]



