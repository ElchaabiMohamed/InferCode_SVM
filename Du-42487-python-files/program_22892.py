def reverse_list(l):
   l2 = []
   if len(l) == 1:
      l2.append(l.pop(-1))

   while len(l) >= 1:
      l2.append(l.pop(-1))

   return l2