def union(a,b):
  i = 0 
  d = {}
  while i < len(a):
    d[a[i]] = True 
    i = i + 1

    k = 0 
    while k < len(b):
      if b[k] not in d:
        d[b[k]] = True 
      k = k + 1

    return d  
    


if __name__ == "__main__":
  print(union([1,2,3],[3,4,5]))

