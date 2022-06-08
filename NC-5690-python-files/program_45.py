def doubleLettre(mot):
  reponse=False
  aux=''
  for c in mot: 
    if c==aux:
      reponse=True
    aux=c
  return reponse