def swap_keys_values(a):
   newdict = {}
    
   for l, m in list(a.items()):
      newdict[m] = l
   return newdict
	
if __name__ == '__main__':
	main()
