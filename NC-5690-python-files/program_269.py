def maximum(liste):
   if len(liste)==0:
      res=None
   else:
      res=liste[0]
      for i in liste:
         if res<liste[0]:
            res=liste[0]
   return res