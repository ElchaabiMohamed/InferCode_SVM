def selection_sort(a):
  for i in range(len(a)):
    j = 1
    if a[j] > a[i]:
      tmp = a[i]
      a[i] = a[j]
      a[j] = tmp
    j += 1 
  return a  
