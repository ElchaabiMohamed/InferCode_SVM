def permutationChaine(s):
  res=''
  for i in range(0,len(s)-1,2):
    res+=s[i+1]
    res+=s[i]
  if len(s)%2!=0:
    res+=s[-1]
  return res