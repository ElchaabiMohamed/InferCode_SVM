def fibonacci(s):
   if s <=1:
      return 1
   else:
      return fibonacci(s - 1) + fibonacci(s - 2)
