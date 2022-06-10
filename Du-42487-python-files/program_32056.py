def swap_unique_keys_values(d):
   tempd = {}
   alltupps = []
   for k,v in list(d.items()):
      alltupps.append(v,k)

   return alltupps

# if __name__ == "__main__":
#    main()


# what about if you tried to create a new dictionary with only unique values in it?
# no, this means you still get the doubles the first time. you need to NEVER get them...