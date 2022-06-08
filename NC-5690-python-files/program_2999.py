def permutationChaine(s):
  res=''
  for i in range(0,len(s)+1,2):
    res=res+s[n+i]+s[i]
  if len(s)%2!=0:
    res=res+s[-1]
  return res