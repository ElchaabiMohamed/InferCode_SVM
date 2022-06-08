def rechercheDicho(liste,val):
  debut=0
  fin=len(liste)-1
  nbAcces=0
  while debut<fin:
    nbAcces+=1
    indice=(debut+fin)//2
    elem=liste[indice]
    if elem==val:
      return (indice,nbAcces)
    elif elem<val:
      debut=indice+1
    else:
      fin=indice-1
  return (None,nbAcces)