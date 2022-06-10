#
def fibonacci(n):
   a, b = 0, 1 
   for num in range(n):
      a, b = b, a + b 
      return a

if __name__ == '__main__':
   print('calling fibonacci(\'fibonacci number\')')
   print(fibonacci(0))
   print(fibonacci(1))
   print(fibonacci(6))