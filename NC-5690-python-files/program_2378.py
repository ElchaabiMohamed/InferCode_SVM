def permutationChaine(s):
  res=""
  for i in range(0,len(s)-1,2):
    res=res+o[i+1]+o[i]
  if (len(s)%2!=0):
    res=res+[-1]
  return res