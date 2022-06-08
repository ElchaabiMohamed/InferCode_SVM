def maximum(liste):
   res=liste[0]
   if len(liste)==0:
      res=None
   else:
      for i in liste:
         if res<liste[0]:
            res=liste[0]
   return res