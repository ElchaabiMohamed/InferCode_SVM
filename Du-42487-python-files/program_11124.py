def selectionsort(m):
   for i in range(len(m)):
      min_j = i
      for j in range(i, len(m)):
         if m[j] < m[min_j]:
            min_j = j
            m[i], m[min_j] = m[min_j], m[i]
