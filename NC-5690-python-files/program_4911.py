def ecart(liste):
   res=0
   if len(liste)==0:
      res=None
   if len(liste)==1:
      res=0
   else:
      max=liste[0]
      min=max
      for elem in range(len(liste)):
         if elem>max:
            max=elem
      for elem in range(len(liste)):
         if elem<min:
            min=elem
   res=res+max-min
   return res