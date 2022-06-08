def nbVoyelles(mot):
    Voy=["a","e","u","i","o","y"]
    res=0
    for i in mot:
      if i in Voy:
        res=res+1
    return res