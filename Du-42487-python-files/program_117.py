def power(m, n):
  if m == m ** n:
    return m
  else:   
    m = m ** n
    return power(m, n)

