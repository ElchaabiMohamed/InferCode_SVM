def fibonacci(n):
   if n == 1 or n == 0 :
      return 1

   return  fibonacci(n - 1) + fibonacci(n - 2)