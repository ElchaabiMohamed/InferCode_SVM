def maximum(liste):
  max=liste[1]
  for i in range(1,len(liste)): 
    if liste[i]>max:
      max=liste[i]	
  return max