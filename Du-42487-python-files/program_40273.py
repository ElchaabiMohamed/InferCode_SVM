def minimum(list):
   if len(list) == 1:
      return list[0]
   else:
      if list[-1] < list[0]:
         list.remove[-1]
      else:
         list.remove[0]
      return minmum(list)
