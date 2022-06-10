def minimum(l, i=0):
   j = i
   while j < len(l) and l[j] > l[-1]:
      j += 1

   if j < len(l):
      tmp = l[i]
      l[i] = l[j]
      l[j] = tmp
      
   if j > len(l):
      return l[0]
   
   return minimum(l, i + 1)