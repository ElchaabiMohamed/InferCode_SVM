def swap_unique_keys_values(a):
   newdict = {}
    
   for l, m in list(a.items()):
      if m not in newdict:
         newdict[m] = l
      else:
         del newdict[m]
   return newdict
	
if __name__ == '__main__':
	main()
