def maximum(liste):
  maxVal=liste[0]
  for i in range(0,len(liste)+1): 
    if liste[i]>maxVal:
      maxVal=liste[i]	
  return maxVal