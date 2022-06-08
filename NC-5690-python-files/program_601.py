def nbVoyelles(mot):
   for lettre in mot:
      if lettre in 'aeiouy':
         res=res+1
   return res