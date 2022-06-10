def minimum(list):
   smallest = list[0]
   
   for nr in list:
      if nr < smallest:
         smallest = nr
   
   return smallest
   
   
   