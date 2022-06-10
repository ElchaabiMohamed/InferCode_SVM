def power(m, n):
   if n == 0:
      return 1
   else:
      return power(m , n - 1) * m