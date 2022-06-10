def selectionsort(m):
   for i in range(len(m)):
      n = i
      for j in range(i, len(m)):
         if m[j] < m[n]:
            n = j
      m[i], m[n] = m[n], m[i]

