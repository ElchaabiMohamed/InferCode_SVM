def nbVoyelles(mot):
   res=0
   if mot==0:
      res=0
   else:
      for lettre in 'aeiouy':
         res=res+1
   return res