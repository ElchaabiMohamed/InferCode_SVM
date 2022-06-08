def permutationChaine(s):
  cpt=''
  for elem in s:
    cpt[elem]=cpt[elem]+1
  return cpt