def permutationChaine(o):
  res=""
  for i in range(o,len(o)-1,2):
    res=res+o[i+1]+s[i]
  if (len(o)%2!=0):
    res=res+[-1]
  return res