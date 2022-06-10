def power(m, n):
  if m == 1:
    return m
  else:   
    m = m ** n
    return power(m, n)

