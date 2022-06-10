import sys

def swap_unique_keys_values(d):
   seen = []
   unseen = []
   for v in list(d.keys()):
      va = d[v]
      if va in unseen:
         seen.append(va)
      else:
         unseen.append(va)
      out = {v:k for k,v in list(d.items()) if v in unseen}
   return out



def main():
   d = {'a': '4', 'b': '7', 'c': '10', 'd': '7'}
   print((swap_unique_keys_values(d)))

if __name__ == '__main__':
	main()