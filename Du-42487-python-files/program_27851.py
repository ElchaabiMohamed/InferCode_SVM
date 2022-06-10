
def reverse(a):
   b = []
   i = 0
   while i < len(a):
      b.append(a[len(a) - i - 1])
      i = i + 1

   return b
