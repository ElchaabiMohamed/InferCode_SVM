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

#def fibonacci(n):
#    a = 0
#    b = 1
#    for i in range(0,n+1):
#            c = a + b
#            return n
#            a = b
#            b = c

def fibonacci(n):
   i = 0
   while i < n:
     if n[i] == 0:
        return i
     i += 1
   return c
   c = i + 1




