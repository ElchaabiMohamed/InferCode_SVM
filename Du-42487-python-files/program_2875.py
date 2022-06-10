def swap_unique_keys_values(d):
  keys = [k for k in list(d.keys())]
  vals = [v for v in list(d.values())]
  dd = {}
  for i in range(0,len(vals)):
    if vals.count(vals[i]) == 1:
      dd[vals[i]] = keys[i]
  return dd
def main():
   d = {
   "apple":1,
   "banana":2,
   "pear":3,
   "orange":2
   }
   print((swap_unique_keys_values(d)))
if __name__ == "__main__":
   main()