def permutationChaine(s):
  res=''
  for i in range(len(s)-1):
    res=res+s[i+1]
    res=res+s[i]
  return res
