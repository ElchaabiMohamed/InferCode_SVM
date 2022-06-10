def swap_keys(d):
   d = {v: k for (k,v) in list(d.items())}
   return d

def main():
   d = {
   "apple":1,
   "banana":2,
   "orange":3,
   "pear":4,
   "cherry":5
   }
   print((swap_keys(d)))
if __name__ == "__main__":
   main()
