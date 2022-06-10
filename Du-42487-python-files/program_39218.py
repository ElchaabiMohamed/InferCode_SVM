i = 0
while i < len(a):
   p = find_smallest_position(a,i)
   swap(a,i,p)
   i = i + 1