def sumup(n):
   if n == 1:
      return 1

   if n != 0:
      return n + sumup(n-1)
   else:
      return 0