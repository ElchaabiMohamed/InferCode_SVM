def permutationChaine(s):
  res=''
  for i in range(len(s)):
    res=res+s[i+1]
    res=res+s[i]
  return res