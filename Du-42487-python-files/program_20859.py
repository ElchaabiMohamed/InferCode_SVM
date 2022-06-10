#

def fibonacci(n):
   a, b = 0, 1 
   for num in range(n):
      a, b = b, a + b 
      return a

