def power (m, n):
   if n == 0:
      return 1
   else:
      return sum(m * (m, n - 1))