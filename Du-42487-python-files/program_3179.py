def reverse_list(m):
   if len(m) == 0:
      return []
   else:
      return [m[-1]] + reverse_list(m[:-1])
