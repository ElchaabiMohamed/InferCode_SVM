def union(a, b):
   ab = a + b
   c = []
   for i in ab:
      if i not in c:
         c.append(i) 
   return c


if __name__ == "__main__":
   print(union([1, 2, 3], [3, 4, 5]))
