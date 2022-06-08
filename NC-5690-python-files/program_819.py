def doubleChiffre(nombre):
  temp = str(nombre)
  for i in range (len(temp)-1):
    if temp[i]==temp[i+1]:
      return True
  return False