def power(m, n):
  if m == 0:
    return 1
  else:   
    m = m ** n
    return power(m-1, n)

