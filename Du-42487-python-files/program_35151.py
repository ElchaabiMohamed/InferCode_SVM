import time
skip = []
"""d = {
"apple":1,
"banana":2,
"pear":3,
"orange":2
}"""
def swap_unique_keys_values(d):
   global skip
   check = []
   for x in list(d.keys()):
      if d[x] not in check:
         check.append(d[x])
      else:
         skip.append(d[x])
   d = [seen(k,v) for k,v in list(d.items())]
   print(d)
def seen(k,v):
   global skip
   if v in skip:
      return k,v
   else:
      return v,k
"""def result():
   #print(swap_unique_keys_values(d))
   d = [seen(k,v) for k,v in d.items()]
   print(d)"""
