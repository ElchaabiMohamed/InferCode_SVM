def nbVoyelles(mot):
    nb = 0
    voy = ['a','e','i','o','u','y']
    for v in mot:
      if v in voy:
        nb+=1
 
    return nb