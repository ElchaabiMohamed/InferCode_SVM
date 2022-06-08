def nombresPremiers(n):
    res=[]
    nb=2
    while len(res)<n:
      ok=True
      i=0
      while i<len(res) and ok:
        if nb%res[i]==0:
          ok=False
        i+=1
      if ok:
        res.append(nb)
      nb+=1
    return res
  