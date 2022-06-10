import time
def countdown(num):
    for n in range(num):
        print(n)
        time.sleep(.100)
    print("LIFT OFF!")
def search(steve,letter):
    if letter in steve:
       return True
    else:
       return False
def index(steve,letter):
     return steve.find(letter)

def fibonacci(n):
   inc1 = 1
   inc2 = 0
   inc3 = ""
   l1 = [0]
   for fib in range(0,n + 1):
       inc3 = inc2
       inc2 = inc1
       inc1 = inc3 + inc2
       l1.append(inc3)
   return l1[n]



n = int(input())
print(fibonacci(n))


if __name__ == '__main__':
#add something for Fibonacci
   print("testintg but not really")
