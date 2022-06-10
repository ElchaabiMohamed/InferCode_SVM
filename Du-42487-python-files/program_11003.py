def reverse_list(a):
   b = []
   i = 0
   while i < len(a):
      b.append(a[-i - 1])
      i += 1
   return(b)
