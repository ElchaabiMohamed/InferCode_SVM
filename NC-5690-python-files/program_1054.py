def permutationChaine(s):
  res=''
  for i in range(0,len(s)-1):
    res=res+s[i+1]
    res=res+s[i]
  res=res+s[len(s)-1]
  return res