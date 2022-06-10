def fibonacci(s):
   if s == 0:
      return 1
   else:
      return fibonacci(s-1) + fibonacci(s+5)
