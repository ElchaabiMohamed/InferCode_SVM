a = []
i = 0

while i < len(a):
   a.append(sys.stdin.read())
   i = i + 1

def insertion_sort(a, is_less_than):
   i = 1
   while i < len(a):
      v = a[i]
      j = i
      while 0 < j and is_less_than(v, a[j - 1]):
         a[j] = a[j - 1]
         j = j - 1
      a[j] = v

      i = i + 1
