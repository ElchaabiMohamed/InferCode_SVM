def indiceInsertion(sc,scores):
  i = 0
  res = None
  while i < len(scores) and res == None:
    if sc >= scores[i]:
      res = i
    i = i + 1
  if i == len(scores):
    res = len(scores)
  return res