"""
skip = []
def main():
   d = {
   "apple":1,
   "banana":2,
   "pear":3,
   "orange":2
   }
   swap_unique_keys_values(d)
def swap_unique_keys_values(d):
   global skip
   check = []
   for x in d.keys():
      if d[x] not in check:
         check.append(d[x])
      else:
         skip.append(d[x])
   d = [seen(k,v) for k,v in d.items()]
   print(d)
def seen(k,v):
   global skip
   if v in skip:
      return k,v
   else:
      return v,k
if __name__ == "__main__":
   main()"""
#The above commented out solution works but einstein wants me to completely ignore ANY sort of duplicate and not re-assign even with one
def swap_unique_keys_values(d):
   d = {v: k for (k,v) in list(d.items())}
   return d
