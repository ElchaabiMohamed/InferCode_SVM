def minimum(liste):
   if len(liste)==0:
      res=0
   else:
      rest=liste[0]
      for i in range(len(liste)):
        if(liste[0])<res:
            res=(liste[0])
   return res