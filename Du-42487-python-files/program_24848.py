import sys

def swap_unique_keys_values(d):
   keys = []
   values = []
   dict_keys = []
   dict_values = []
   dump = []
   
   for (k, v) in list(d.items()):
      keys.append(k)
      values.append(v)

   for num in values:
      test = num
      values = values[1:]
      
      if test in values:
         dump.append(test)
     
      elif test not in values and test not in dump:
         dict_keys.append(test)
         dict_values.append(keys[0])
      keys = keys[1:]

   d = {}
   for i in range(0, len(dict_keys)):
      d[dict_keys[i]] = dict_values[i]

   return(d)

def main():
   my_dict = {'a' : 4, 'b' : 7, 'c' : 10, 'd' : 7}
   print((swap_unique_keys_values(my_dict)))

if __name__ == '__main__':
    main()