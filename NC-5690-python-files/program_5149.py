def sommeNbPairs(liste):
   res=0
   for x in liste:
      if x%2==0:
         res+=x
   return res