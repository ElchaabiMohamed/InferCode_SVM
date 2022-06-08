scores=[352100,325410,312785,220199,127853]
joueurs=['Batman','Robin','Batman','Jocker','Batman']

def listeDecroissante(scores):
  res=True
  i=0
  while i<len(scores)-1 and res:
    if scores[i]<=scores[i+1]:
      res=False
  return res
    