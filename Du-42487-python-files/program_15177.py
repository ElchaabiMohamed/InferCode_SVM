def union(a,b):
  i = 0 
  dic = {}
  while i < len(a):
    dic[a[i]] = True 
    i = i + 1

    k = 0 
    while k < len(b):
      if not (b[k] in dic):
        dic[b[k]] = True 
      k = k + 1

    return dic  
    


if __name__ == "__main__":
  print(union([1,2,3],[3,4,5]))

