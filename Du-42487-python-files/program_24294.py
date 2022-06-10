def union(a,b):
  i = 0 
  dic = {}
  while i < len(a):
    dic[a[i]] = True 
    i = i + 1

    j = 0 
    while j < len(b):
      if not (b[j] in dic):
        dic[b[j]] = True 
      j = j + 1

    return dic  
    




