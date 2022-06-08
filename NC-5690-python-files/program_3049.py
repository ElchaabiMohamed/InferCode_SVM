def reconstruirePartielle(s,n):
  res =''
  for i in range (0,len(s),n):
    res = res + s[i]
  return res