def nbVoyelles(mot):
   res=0
   if len(mot)==0:
      res=0
   else:
       for lettre in mot:
          if lettre in 'aeiouy':
             res=res+1
   return res