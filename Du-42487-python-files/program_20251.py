def swap_unique_keys_values(d):
   keys = []
   values = []
   dict_keys = []
   dict_values = []
   dump = []
   
   for (k, v) in list(d.items()):
      keys.append(k)
      values.append(v)
#   print(keys)
#   print(values)
   for num in values:
      test = num
#      print (test)
      values = values[1:]
#      print (values)
      
      if test in values:
         dump.append(test)
#         print('dump', dump)
      
      elif test not in values and test not in dump:
         dict_keys.append(test)
         dict_values.append(keys[0])
      keys = keys[1:]
#   print(dict_keys)
#   print(dict_values)

   d = {}
#   i = 0
   for i in range(0, len(dict_keys)):
      d[dict_keys[i]] = dict_values[i]
#      i = i + 1
#   print(d)

   return(d)

if __name__ == '__main__':
    main()

