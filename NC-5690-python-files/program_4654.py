def permutationChaine(o):
  res=""
  for i in range(0,len(s)-1,2):
    res=res+s[i+1]+s[i]
  if (len(s)%2!=0):
    res=res+[-1]
  return res