import sys

def swap_unique_keys_values(d):
   new_d = {}
   t = []
   #new_d = {v:k if v not in new_d else  for (k,v) in d.items()}
   #print(t)
   for (k,v) in list(d.items()):
      if v not in new_d:
         new_d[v] = k
      else:
         t.append(v)
         
   for v in t:
      del new_d[v]
         
   return new_d
def main():
   new_dict = swap_unique_keys_values(my_dict)

if __name__ == "__main__":
   main()
