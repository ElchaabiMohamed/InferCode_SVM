def swap_unique_keys_values(d):
   tempd = {}
   alltupps = []
   newlist = []
   for k,v in list(d.items()):
      alltupps.append((v,k))
   alltupps = sorted(alltupps)
   i = 0
   while i < len(alltupps) - 1:
      # print(alltupps[i][0])
      if alltupps[i][0] != alltupps[i + 1][0]:
      	  newlist.append(alltupps[i])
      else:
      	i += 1
      i += 1
   if alltupps[-2][0] != alltupps[-1][0]:
   	  newlist.append(alltupps[-1])
   return dict(newlist)

def main():
   print((swap_unique_keys_values({'a' : 4, 'b' : 7, 'c' : 10, 'd' : 7})))

if __name__ == "__main__":
   main()


# what about if you tried to create a new dictionary with only unique values in it?
# no, this means you still get the doubles the first time. you need to NEVER get them...