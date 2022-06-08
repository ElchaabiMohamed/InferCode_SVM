def ecart(liste):
   res=0
   if len(liste)==0:
      res=None
   if len(liste)==1:
      res=0
   else:
      max=liste[0]
      min=max
      for i in range(len(liste)):
         if liste[i]>max:
            max=liste[i]
      for i in range(len(liste)):
         if liste[i]<min:
            min=liste[i]
   res=max-min
   return res