def nbVoyelles(mot):
  listeVoyelles = ["a","e","i","o","u","y"]
  res = 0
  for c in mot:
    if c in listeVoyelles:
      res += 1
  return res