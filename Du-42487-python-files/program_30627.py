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


def index(str,letter):
   i = 0
   while i < len(str):
      if str[i] == letter:
        return i
      i += 1
   return - 1

def fib (n): 
    if( n == 0):
        return 0
    else:
        x = 0
        y = 1
        for i in range(1,n):
            z = (x + y)
            x = y
            y = z
            return y

for i in range(10):
    print((fib(i)))

